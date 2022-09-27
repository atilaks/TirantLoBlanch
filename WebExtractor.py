import requests
from bs4 import BeautifulSoup

"""
EXTRACTOR DE WEB

Toma como input la URL de la página de acuerdos de 2020
del portal de contratación de Navarra, simplificada la
solicitud mediante Requests, para devolver un objeto
BeautifulSoup de tipo texto basado en HTML.

Se aísla de la URL el valor que asigna el número de pagina
para poder recorrerse posteriormente con un FOR.
"""

def WebExtractor(incomplete_url, page=""):
    complete_url = requests.get(incomplete_url+str(page))
    soup = BeautifulSoup(complete_url.text, 'html.parser')
    return soup