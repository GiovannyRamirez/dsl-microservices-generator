from os import listdir, path
from entity_codegen_modified import main

folder = path.dirname(__file__)
entidades = listdir(folder + "/entidades/")

for entity in entidades:
    main(False, entity)