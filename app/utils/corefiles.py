import json
import os

#Lee los json, path funciona como un parametro reemplazable dependiendo del json que se quiera leer
def readDataFile(path):
    """Función genérica para leer cualquier archivo JSON."""
    try:
        with open(path, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

#Escribe los json, path y data funcionan como parametros reemplazables dependiendo del json que se quiera escribir
def writeDataFile(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

#Revisa que un json exista, este fue un codigo que me proporciono la ia
def initialize_file(path):
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        writeDataFile(path, {})