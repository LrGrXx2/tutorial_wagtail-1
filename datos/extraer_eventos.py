'''
Trabajo: 
* Inspeccionar la estructura de la web
* Extraer los datos de las eventos con xpath
'''

import requests
from lxml import html
from urllib.parse import urljoin
import json

headers = {"Accept-Language": "es-es,es;q=0.5"}



def datos_event(event):
    # datos a devolver
    datosE = {}

    elementos = event.xpath(".//td")
    nombre = elementos[0]
    descripcion = elementos[1]
    imagen = elementos[2]
    fecha_inicio = elementos[3]

    # nombre
    nombre_ = nombre.xpath(".//a/text()")[0]
    datosE['nombre'] = nombre_

    # descripcion
    descripcion_ = nombre.xpath(".//a/text()")[0]
    datosE['descripcion'] = descripcion_

    # imagen
    imagensrc = imagen.xpath(".//img/@src")[0]
    datosE['imagen'] = imagensrc

    # fecha_inicio (yyyy/dd/mm)
    fecha_inicio = nombre.xpath(".//span/text()")[0].strptime(fecha_inicio, "%Y%m%d%")
    datosE['fecha_inicio'] = fecha_inicio

    
    #datosE.update(detalle(url))

    return datosE

if __name__ == '__main__':

    url = 'https://www.imdb.com/chart/top/'
    
    response = requests.get(url, headers=headers)
    pagina = html.fromstring(response.text)

    eventos = pagina.xpath("//table[@data-caller-name='chart-top250movie']/tbody/tr")

    # test
    assert(len(eventos) == 250)

    datosE = [datos_event(e) for e in eventos]
    json.dump(datosE, open('datos_eventos.json', 'w'))
