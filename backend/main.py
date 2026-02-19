from fastapi import FastAPI

#Crear un objeto que represente mi aplicación (mi API)

app = FastAPI() # Llama al método constructor de FastAPI

@app.get("/")

def saludar():
    saludo = {
        "mensaje" : "Hola Mundo!!! API OK"
    }

    return saludo

@app.get("/despedir")

def despedirse():
    mensaje = {
        "mensaje" : "Adiós mundo cruel!!! API OK"
    }

    return mensaje