# tutorial_wagtail-1
## Descripción
Web de datos realizada con Wagtail.
En ella podemos ver el listado de las 250 mejores películas (extraidas de la web de IMDb: https://www.imdb.com/chart/top/), un listado de las fiestas de Santa Cruz de Tenerife (sacadas de un json del ayuntamiento de ese lugar), diferentes opciones de viajes a Santa Cruz de Tenerife con distintas compañías, y algunas noticias sobre el mundo del entretenimiento.

**Nombre del admin:** admin / **Contraseña de admin:** root

## ¿Cómo lo instalo y hago funcionar?
### Windows
(ATENCIÓN) Deberemos tener en nuestro ordenador la aplicación "GitBash" u otra del estilo para que el cmd reconozca los comandos de Git, y Python.
1. Nos posicionamos donde queramos tener la capeta en el cmd (con cd)
2. Copiamos el enlace del repositorio git donde está el trabajo
3. En el cmd escribimos: git clone https://github.com/LrGrXx2/tutorial_wagtail-1.git
4. Nos posicionamos dentro del proyecto en el cmd (con cd)
5. Creamos el entorno virtual (py -m venv env)
6. Activamos el entorno virtual (env\Scripts\activate.bat)
7. Instalamos los requisitos (pip install -r requirements.txt)
8. Dentro del entorno: py manage.py runserver
9. En google buscamos: http://localhost:8000/ (número indicado al ejecutar el runserver (Starting development server at http://127.0.0.1:8000/) ese es el 8000)
10. Cuando queramos pararlo: Ctrl + c (en el cmd)

### Linux/Mac
(ATENCIÓN) Deberemos tener en nuestro ordenador la aplicación "GitBash" u otra del estilo para que el cmd reconozca los comandos de Git, y Python.
1. Nos posicionamos donde queramos tener la capeta en el cmd (con cd)
2. Copiamos el enlace del repositorio git donde está el trabajo
3. En el cmd escribimos: git clone https://github.com/LrGrXx2/tutorial_wagtail-1.git
4. Nos posicionamos dentro del proyecto en el cmd (con cd)
5. Creamos el entorno virtual (python3 -m venv env)
6. Activamos el entorno virtual (source tutorial-env/bin/activate)
7. Instalamos los requisitos (pip install -r requirements.txt)
8. Dentro del entorno: py manage.py runserver
9. En google buscamos: http://localhost:8000/ (número indicado al ejecutar el runserver (Starting development server at http://127.0.0.1:8000/) ese es el 8000)
10. Cuando queramos pararlo: Ctrl + c (en el cmd)
