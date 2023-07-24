
from database.Hijo import listarHijos, getHijo, cambiarEstado, modificarHijo
from fastapi import APIRouter, Request
import pandas as pd
from database.conexion import session
routerHijo = APIRouter()


# creamos las diferentes rutas de manejo para cada caso





@routerHijo.post('/obtener')
async def obtenerHijo(request: Request):
    data = await request.json()
    id_hijo  = data.get('id_hijo')
    hijo = await getHijo(id_hijo=id_hijo)
    return hijo


@routerHijo.get('/all')
async def allHijos():
    hijos = await listarHijos()
    session.close()
    return hijos

@routerHijo.post('/estado')
async def changeEstado(request:Request):
    try:
        data = await request.json()
        id_hijo = data.get('id_hijo')
        await cambiarEstado(id_hijo=id_hijo)
        session.close()
        return {"status":1}
    except:
        return {"status":0}
    


@routerHijo.post('/update')
async def updateHijo(request:Request):
    try:
        Hijo = await request.json()
        await modificarHijo(Hijo=Hijo)
        session.close()
        return {"status":1}
    except:
        return {"status":0}