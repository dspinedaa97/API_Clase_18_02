# Demo API

Proyecto de demostración para el manejo de API en Python

## Front End

Se emplea una aplicación simple como frontend (HTML, js, css)

## BackEnd

Con la biblioteca FastAPI (para crear la API)

1. Crear el Ambiente virtual: python -m venv tutorial-env
2. Instalar vunicorn (para publicar la API)
    2.1. pip install fastapi uvicorn

Ejecutar el servidor: uvicorn main:app --reload

http://127.0.0.1:8000/docs muestra la documentación de la API

Instalar geopandas y requests

https://github.com/paulocoronadoud/demoAPI2.git