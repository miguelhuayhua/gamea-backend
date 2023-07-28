from database.AdultoMayor import listarAdulto, getAdulto, cambiarEstado, modificarAdulto
from database.Hijo import getHijosByIdAdulto
from fastapi import APIRouter, Request
import pandas as pd
from database.conexion import session
routerAdulto = APIRouter()


# creamos las diferentes rutas de manejo para cada caso


@routerAdulto.get('/npmunicos')
async def all():
    data = await listarAdulto()
    dictAdulto = []
    for adulto in data:
        dict = adulto.__dict__
        dict.pop('_sa_instance_state')
        dictAdulto.append(dict)
    dataframe = pd.DataFrame.from_records(dictAdulto)
    if (len(data) != 0):
        nombres = dataframe['nombre'].unique()
        paterno = dataframe['paterno']
        materno = dataframe['materno']
        nombres = nombres[nombres!='']
        apellidos = pd.concat([paterno, materno], axis=0).unique()
        apellidos = apellidos[apellidos !='']
        session.close()
        return {'nombres': nombres.tolist(), 'apellidos': apellidos.tolist()}
    else:
        return {'nombres': [], 'apellidos':[]}


@routerAdulto.post('/get')
async def obtenerAdulto(request: Request):
    data = await request.json()
    id_adulto  = data.get('id_adulto')
    adulto = await getAdulto(id_adulto=id_adulto)
    hijos = await getHijosByIdAdulto(adulto.id_adulto)
    session.close()
    return {"adulto":adulto, "hijos":hijos}


@routerAdulto.get('/all')
async def allAdultos():
    adultos = await listarAdulto()
    session.close()
    return adultos

@routerAdulto.post('/estado')
async def changeEstado(request:Request):
    try:
        data = await request.json()
        id_adulto = data.get('id_adulto')
        await cambiarEstado(id_adulto)
        session.close()
        return {"status":1}
    except:
        return {"status":0}
    


@routerAdulto.post('/update')
async def updateAdulto(request:Request):
    try:
        adulto = await request.json()
        await modificarAdulto(adulto=adulto)
        session.close()
        return {"status":1}
    except:
        return {"status":0}