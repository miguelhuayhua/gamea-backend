from fastapi import FastAPI
import databases
import asyncpg
from database.conexion import database
# importamos todas las rutas que creamos en la carpeta "routes"
from routes.adulto import router

app = FastAPI()

# Credenciales de la base de datos
# Conexion de la base de datos


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# colocado de las rutas en la aplicación principal
app.include_router(router, prefix='/adulto')
