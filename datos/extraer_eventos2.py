
import json
from urllib import request
 
data = '''
[
  {
        "nombre": "\"Marathon Internacional Santa Cruz de Tenerife\"",
        "descripcion": "\"*fecha no confirmada. Distancias: 42197m, 21097m, 8000m, Asfalto. Más información próximamente<link http://maratondetenerife.com/ _blank - \"ir a..\"> <strong>aquí</strong></link>\"",
        "imagen": "https://www.santacruzdetenerife.es/web/fileadmin/user_upload/running.jpg",
        "fecha_inicio": 20191110,
      }
]'''
 
url = "https://www.santacruzdetenerife.es/opendata/dataset/f38a3086-8d4c-4c6a-943e-629056b66f01/resource/95a65af3-5f11-4041-a418-45afcc5e7686/download/agendacultural.json"
#info = json.loads(data)
access_token = "my_token"
 
result = request.get(url,headers={"Content-Type":"application/json","Authorization": "Bearer {}".format(access_token)})
json = result.json()
eventos = json["data"][0-3]
print(eventos)