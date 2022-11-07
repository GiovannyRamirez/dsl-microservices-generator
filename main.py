from os import listdir, path
from entity_codegen_modified import main as generateFiles

folder = path.dirname(__file__)
entidades = listdir(folder + "/entidades/")
main_files = {}

for entity in entidades:
    main_files[entity.split(".ent")[0]] = entity.split(".ent")[0]
    generateFiles(False, entity, False)

generateFiles(False, False, main_files)