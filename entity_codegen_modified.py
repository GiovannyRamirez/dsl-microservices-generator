"""
An example how to generate angularjs code from textX model using jinja2
template engine (http://jinja.pocoo.org/docs/dev/)
"""
from os import mkdir
from os.path import exists, dirname, join
import jinja2
from entity_test import get_entity_mm


def main(debug=False, file_name=False, files=False):

    def is_entity(n):
        """
        Test to prove if some type is an entity
        """
        if n.type in entity_model.entities:
            return True
        else:
            return False

    def javatype(s):
        """
        Maps type names from PrimitiveType to Javascript.
        """
        return {
                'integer': 'int',
                'string': 'String'
        }.get(s.name, s.name)

    templates_folder = "./templates/"
    entities_folder = "./entidades/"
    general_folder = "./proyecto_generado/"

    if file_name:
        folder_to_export = general_folder + file_name.split(".ent")[0] + 's'
    else:
        folder_to_export = general_folder

    # Create output folder
    this_folder = dirname(__file__)
    srcgen_folder = join(this_folder, folder_to_export)
    if not exists(srcgen_folder):
        mkdir(srcgen_folder)

    # Initialize template engine.
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    # Register filter for mapping Entity type names to Java type names.
    jinja_env.tests['entity'] = is_entity
    jinja_env.filters['javatype'] = javatype

    entity_mm = get_entity_mm(debug)  

    if not file_name:
        main_folder = join(this_folder, general_folder)
        # Load nginx template
        template = jinja_env.get_template(templates_folder+'nginx.template')
        # For each entity add its respectively route in file [nginx.conf]
        with open(join(main_folder,
            "nginx.conf"), 'w') as f:
            f.write(template.render(entities=files))

        # Load docker-compose template
        template = jinja_env.get_template(templates_folder+'docker-compose.template')
        # For each entity add its respectively build and link in file [docker-compose.yml]
        with open(join(main_folder,
            "docker-compose.yml"), 'w') as f:
            f.write(template.render(entities=files))

        # Load README template
        template = jinja_env.get_template(templates_folder+'README.template')
        # For each entity add its respectively field in file [README.md]
        with open(join(main_folder,
            "README.md"), 'w') as f:
            f.write(template.render(entities=files))
    else:
        # Build Entity model from file_name file
        entity_model = entity_mm.model_from_file(join(this_folder, entities_folder + file_name))
        # Load app template
        template = jinja_env.get_template(templates_folder+'app.template')
        for entity in entity_model.entities:
            # For each entity generate file [app.py]
            with open(join(srcgen_folder,
                "app.py"), 'w') as f:
                f.write(template.render(entity=entity))

        # Load config_app template
        template = jinja_env.get_template(templates_folder+'config_app.template')
        for entity in entity_model.entities:
            # For each entity generate file [config_app.py]
            with open(join(srcgen_folder,
                "config_app.py"), 'w') as f:
                f.write(template.render(entity=entity))

        # Load models template
        template = jinja_env.get_template(templates_folder+'models.template')
        for entity in entity_model.entities:
            # For each entity generate file [models.py]
            with open(join(srcgen_folder,
                "models.py"), 'w') as f:
                f.write(template.render(entity=entity))

        # Load requerimientos template
        template = jinja_env.get_template(templates_folder+'requerimientos.template')
        for entity in entity_model.entities:
            # For each entity generate file [requerimientos.txt]
            with open(join(srcgen_folder,
                "requerimientos.txt"), 'w') as f:
                f.write(template.render(entity=entity))

        # Load Dockerfile template
        template = jinja_env.get_template(templates_folder+'Dockerfile.template')
        for entity in entity_model.entities:
            # For each entity generate file [Dockerfile]
            with open(join(srcgen_folder,
                "Dockerfile"), 'w') as f:
                f.write(template.render(entity=entity))


if __name__ == "__main__":
    main()
