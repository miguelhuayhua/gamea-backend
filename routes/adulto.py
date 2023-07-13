from database.AdultoMayor import listarAdulto, getAdulto
from models.AdultoMayor import AdultoMayor
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


@routerAdulto.post('/obtener')
async def obtenerAdulto(request: Request):
    data = await request.json()
    id_adulto  = data.get('id_adulto')
    adulto = await getAdulto(id_adulto=id_adulto)
    hijos = await getHijosByIdAdulto(adulto.id_adulto)
    
    return {"adulto":adulto, "hijos":hijos}