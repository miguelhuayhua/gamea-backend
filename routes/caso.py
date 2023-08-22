from database.Caso import getUltimoCaso, allCasos, cambiarEstado, modificarCaso,getCaso
from database.AdultoMayor import listarAdulto
from database.Seguimiento import insertSeguimiento, allSeguimientoByCaso
from database.Hijo import listarHijos
from database.Citacion import allCitacionByCaso, insertCitacion
from database.Citado import insertCitado
from fastapi import APIRouter, Request

from database.conexion import session
from fastapi.responses import FileResponse
import tempfile

import pandas as pd


routerCaso = APIRouter()


# creamos las diferentes rutas de manejo para cada caso
@routerCaso.get('/all')
async def allCaso():
    casos =  await allCasos()
    session.close()
    return casos


@routerCaso.post('/get')
async def obtenercaso(request: Request):
    data = await request.json()
    id_caso  = data.get('id_caso')
    caso = await getCaso(id_caso=id_caso)
    return caso



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
    dataHijos = await listarHijos()
    hijos = []
    for hijo in dataHijos:
        dict = hijo.__dict__
        dict.pop('_sa_instance_state')
        hijos.append(dict)
    dataAdultos = await listarAdulto()
    adultos = []
    for adulto in dataAdultos:
        dict = adulto.__dict__
        dict.pop('_sa_instance_state')
        adultos.append(dict)
    dataframeAdultos = pd.DataFrame.from_records(adultos)
    unido1 = pd.merge(dataframeAdultos, dataframeCasos, on="id_adulto", how="inner")
    unido1['nro_referencia'] = unido1['nro_referencia'].astype(str)
    unido1['ult_modificacion_y'] = unido1['ult_modificacion_y'].dt.strftime('%Y-%m-%d %H:%M:%S')    
    unido1['ult_modificacion_x'] = unido1['ult_modificacion_x'].dt.strftime('%Y-%m-%d %H:%M:%S')    
    unido1['f_nacimiento'] = pd.to_datetime(unido1['f_nacimiento'], format='%Y-%m-%d').dt.strftime('%Y-%m-%d')
    unido1.reindex(['nombre, paterno, materno'])
      # Crea un archivo temporal
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        # Guarda el DataFrame en el archivo temporal en formato Excel
        unido1.to_excel(temp_file.name, sheet_name='hoja1', index=False, engine='xlsxwriter')

    # Envía el archivo como respuesta utilizando FileResponse
    return FileResponse(temp_file.name, filename='archivo.xlsx')



#SEGUIMIENTOS
@routerCaso.post('/seguimiento/add')
async def addCaso(request:Request):
    try:
        seguimiento = await request.json()
        await insertSeguimiento(seguimiento, seguimiento.get('id_caso'))
        session.close()
        return {"status":1}
    except:
        return {"status":0}
    
@routerCaso.post('/seguimiento/all')
async def allCaso(request:Request):
    data= await request.json()
    id_caso = data.get('id_caso')
    seguimientos = await allSeguimientoByCaso(id_caso)
    session.close()
    return seguimientos


#CITACIONES
@routerCaso.post('/citacion/all')
async def allCitacion(request:Request):
    data = await request.json()
    id_caso = data.get('id_caso')
    citacions = await allCitacionByCaso(id_caso)
    session.close()
    return citacions

@routerCaso.post('/citacion/add')
async def addCitacion(request:Request):
    try:
        print(await request.json())
        citacion = await request.json()
        id_citacion = await insertCitacion(citacion.get('citacion'), citacion.get('id_caso'))
        res = await insertCitado(citacion.get('citados'), id_citacion= id_citacion)
        if (res):
            session.close()
            return {"status":1}
        else:
            return {"status":0, "message":"No se puede generar mas citaciones..."}
    except Exception as e:
        return {"status":0, "message":"Ha ocurido un error en el servidor..."}
    