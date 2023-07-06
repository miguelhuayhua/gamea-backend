from database.AdultoMayor import listarAdulto, insertAdulto
from models.AdultoMayor import AdultoMayor
from fastapi import APIRouter
import pandas as pd
import json
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
    nombres = dataframe['nombre'].unique()
    paterno = dataframe['paterno'].unique()
    materno = dataframe['materno'].unique()

    return {'nombres': nombres.tolist(), 'paterno': paterno.tolist(), 'materno': materno.tolist()}
