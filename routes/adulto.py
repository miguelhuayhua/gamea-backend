from database.AdultoMayor import listar, insert
from models.AdultoMayor import AdultoMayor
from fastapi import APIRouter
import pandas as pd
import json
routerAdulto = APIRouter()


# creamos las diferentes rutas de manejo para cada caso


@routerAdulto.get('/npmunicos')
async def all():
    data = await listar()
    dataframe = pd.DataFrame([record._row for record in data])
    nombres = dataframe[1].unique()
    paterno = dataframe[2].unique()
    materno = dataframe[3].unique()

    print(nombres, paterno, materno)

    return {'nombres': nombres.tolist(), 'paterno': paterno.tolist(), 'materno': materno.tolist()}


@routerAdulto.post('/insert')
async def insertAdulto(adultoMayor: AdultoMayor):
    return adultoMayor.dict()
