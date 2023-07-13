from database.Caso import getUltimoCaso, allCasos, cambiarEstado, modificarCaso
from database.AdultoMayor import listarAdulto
from database.Domicilio import listarDomicilio
from database.Hijo import listarHijos
from fastapi import APIRouter, Request
from database.conexion import session
import pandas as pd
routerCaso = APIRouter()


# creamos las diferentes rutas de manejo para cada caso
@routerCaso.get('/all')
async def allCaso():
    casos =  await allCasos()
    session.close()
    return casos

@routerCaso.get('/getultimo')
async def lastCaso():
    caso = await getUltimoCaso()
    session.close()
    return caso

@routerCaso.post('/estado')
async def changeEstado(request:Request):
    try:
        data = await request.json()
        id_caso = data.get('id_caso')
        await cambiarEstado(id_caso)
        session.close()
        return {"status":1}
    except:
        return {"status":0}
    

@routerCaso.post('/update')
async def updateCaso(request:Request):
    try:
        caso = await request.json()
        await modificarCaso(caso)
        session.close()
        return {"status":1}
    except:
        return {"status":0}
    
@routerCaso.get('/report')
async def reportCaso():
    dataCasos = await allCasos()
    casos = []
    for caso in dataCasos:
        dict = caso.__dict__
        dict.pop('_sa_instance_state')
        casos.append(dict)
    dataframeCasos = pd.DataFrame.from_records(casos)
    print(dataframeCasos)
    dataHijos = await listarHijos()
    hijos = []
    for hijo in dataHijos:
        dict = hijo.__dict__
        dict.pop('_sa_instance_state')
        hijos.append(dict)
    dataframeHijos = pd.DataFrame.from_records(hijos)
    print(dataframeHijos)
    dataAdultos = await listarAdulto()
    adultos = []
    for adulto in dataAdultos:
        dict = adulto.__dict__
        dict.pop('_sa_instance_state')
        adultos.append(dict)
    dataframeAdultos = pd.DataFrame.from_records(adultos)
    print(dataframeAdultos)
    return None