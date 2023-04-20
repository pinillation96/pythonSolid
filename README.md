# Building project locally
Install VirtualEnvironment (one time)

    >python -m pip install virtualenv

Create virtual environment

    >virtualenv virtual_project

1. This will create a virtual environment project folder and install python there.
2. This step can be skipped if you already have the folder locally.

Open virtual environment (Unix type OS)

    >source virtual_project/bin/activate

1. This will activate the virtual environment.  Yous should see `(virtual_project)` to the left of the terminal prompt.
2. This step will be needed each time.

Install requirements
    
    >python -m pip install -r requirements.txt

Install local src/ folder

    >python -m pip install -e src 

# Building Docker image
At the root of the project run

    >docker image build -t YOUR_NAME .

This will create a docker image using the `Dockerfile` with the image name `YOUR_NAME`

Run container

    >docker run YOUR_NAME


## readmeSOLID
    # IMDB Top 250 Movies Scraper

Este script en Python se encarga de raspar la información de las 250 películas mejor calificadas en IMDb utilizando `BeautifulSoup` y guarda los resultados en un archivo CSV. El script sigue los principios SOLID para garantizar un código limpio y fácil de mantener.

## Principios SOLID aplicados

### S - Principio de responsabilidad única

La clase `IMDBScraper` encapsula toda la funcionalidad relacionada con el raspado y procesamiento de datos de las películas. Se crean métodos separados para cada tarea específica (`fetch_data`, `parse_data`, `save_to_csv`), garantizando que cada método tenga una única responsabilidad.

### O - Principio abierto/cerrado

El método `scrape` en la clase `IMDBScraper` utiliza los métodos `fetch_data` y `parse_data` para realizar la funcionalidad de raspado sin modificar su implementación. Si es necesario extender la funcionalidad de raspado, se pueden modificar o agregar nuevos métodos a la clase `IMDBScraper` sin afectar su implementación actual.

### D - Principio de inversión de dependencia

La clase `IMDBScraper` utiliza inyección de dependencia en su constructor para recibir la URL como argumento. Esto permite a la clase ser independiente de detalles concretos y hace que sea más fácil de modificar o reutilizar en diferentes contextos.

### L - Principio de sustitución de Liskov

No hay un caso claro en el script donde se aplique el principio de sustitución de Liskov, ya que no se utilizan clases heredadas ni polimorfismo.

### I - Principio de segregación de interfaces

Tampoco hay un caso claro en el script donde se aplique el principio de segregación de interfaces, ya que no se utilizan interfaces ni clases abstractas.

## Uso

Para ejecutar el script, simplemente ejecuta el siguiente comando en tu terminal:

```bash
python imdb_scraper.py
