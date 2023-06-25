# base de datos
from database.conexion import database


async def insert(data):
    return None


async def all():
    datos = await database.fetch_all('SELECT * FROM adulto_mayor')
    return datos
