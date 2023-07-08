from database.Caso import getUltimoCaso, allCasos, cambiarEstado

from fastapi import APIRouter, Request
from database.conexion import session
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