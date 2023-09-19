from database.Domicilio import getDomicilio, modificarDomicilio, obtenerDomicilioByIdAdulto, insertarDomicilio
from fastapi import APIRouter, Request
import pandas as pd
from database.conexion import session
routerDomicilio = APIRouter()


# creamos las diferentes rutas de manejo para cada caso


@routerDomicilio.post('/get')
async def obtenerDomicilio(request: Request):
    data = await request.json()
    id_adulto  = data.get('id_adulto')
    Domicilio = await getDomicilio(id_adulto=id_adulto)
    session.close()
    return Domicilio


@routerDomicilio.post('/update')
async def updateDomicilio(request:Request):
    try:
        domicilio = await request.json()
        await modificarDomicilio(domicilio=domicilio)
        session.close()
        return {"status":1}
    except:
        session.close()
        return {"status":0}
    
@routerDomicilio.post('/getByIdAdulto')
async def getDomicilioByIdAdulto(request:Request):
    data = await request.json()
    id_adulto = data.get('id_adulto')
    domicilios = await obtenerDomicilioByIdAdulto(id_adulto=id_adulto)
    session.close()
    return domicilios


@routerDomicilio.post('/insert')
async def insertDomicilio(request:Request):
    try:
        domicilio = await request.json()
        await insertarDomicilio(domicilio, domicilio.get('id_adulto'))
        session.close()
        return {"status":1}
    except:
        session.close()
        return {"status":0}