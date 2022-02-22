import json
from urllib import request

url = "https://www.santacruzdetenerife.es/opendata/dataset/f38a3086-8d4c-4c6a-943e-629056b66f01/resource/95a65af3-5f11-4041-a418-45afcc5e7686/download/agendacultural.json"
respuesta = request.urlopen(url)

contenido = respuesta.read()
json_obtenido = json.loads(contenido.decore('utf-8'))

for evento in json_obtenido:
    print(evento) 
    print("\n")



