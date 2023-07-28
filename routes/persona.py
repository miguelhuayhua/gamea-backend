
from database.Persona import cambiarEstado, insertPersona, listarPersonas , getPersona, modificarPersona
from fastapi import APIRouter, Request
import pandas as pd
from database.conexion import session
routerPersona = APIRouter()


# creamos las diferentes rutas de manejo para cada caso





@routerPersona.post('/get')
async def obtenerpersona(request: Request):
    data = await request.json()
    id_persona  = data.get('id_persona')
    persona = await getPersona(id_persona=id_persona)
    return persona


@routerPersona.get('/all')
async def allpersonas():
    personas = await listarPersonas()
    session.close()
    return personas

@routerPersona.post('/estado')
async def changeEstado(request:Request):
    try:
        data = await request.json()
        id_persona = data.get('id_persona')
        await cambiarEstado(id_persona=id_persona)
        session.close()
        return {"status":1}
    except:
        return {"status":0}
    


@routerPersona.post('/update')
async def updatepersona(request:Request):
    try:
        persona = await request.json()
        await modificarPersona(persona = persona)
        session.close()
        return {"status":1}
    except Exception as e:
        print(e)
        return {"status":0}
    


@routerPersona.post('/insert')
async def insertarPersona(request:Request):
    try:
        persona = await request.json()
        id_persona = await insertPersona(data=  persona)
        session.close()
        return {"status":1, 'id_persona' : id_persona}
    except Exception as e:
        print(e)
        return {"status":0}