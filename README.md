## Informática II
###  Laboratorio: Generación de Microservicio
**Integrantes**
- *Anjhelo Giovanny Ramírez Suárez Codigo: 20221099014*
- *Daniel Ricardo Galván Torres Codigo: 20221099003*

This is an example of a simple Entity DSL through python and Jinja2
This project was based on [this example](https://github.com/apdaza/textX_entity2)

You have to have installed
- Python
- pip
- textX
- Jinja2

To create a new entity, follow the next steps:
1. Go to *entidades* folder.
2. Create new file with *.ent* extension.
3. File must to contain next structure:
    ```
    entity [name] {
        [attribute] : [type]
    }
    ```
    - Example:
    ```
    entity domiciliario {
        nombre : string
        apellido : string
        telefono : integer
        placa : string
    }
    ```
4. Save your file.

Run with `python main.py`

As a result of the script generates a structure into *proyecto_generado* folder with next files and folders:
1. Main files of project:
    - README.md.
    - nginx.conf
    - docker-compose.yml
    - ![folder_generados](https://user-images.githubusercontent.com/62915328/200457055-aa951322-2c09-4877-8cbb-a1e1d300af53.PNG)
2. A folder for every entity in *entidades* folder with the next files:
    - app.py
    - config_app.py
    - models.py
    - Dockerfile
    - requerimientos.txt
    - ![archivos_generados](https://user-images.githubusercontent.com/62915328/200457109-7bca9c4d-a693-43d3-abd3-cfaf90a3a7ed.PNG)
