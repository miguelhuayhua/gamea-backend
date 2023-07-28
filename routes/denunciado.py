from database.Denunciado import getDenunciadoByCaso, cambiarEstado, listarDenunciados, getDenunciado

from fastapi import APIRouter, Request
from database.conexion import session
routerDenunciado = APIRouter()



@routerDenunciado.post('/get')
async def obtenerDenunciado(request:Request):
    try:
        data = await request.json()
        id_caso = data.get('id_caso')
        denunciado = await getDenunciadoByCaso(id_caso=id_caso)
        session.close()
        return denunciado
    except:
        return {"status":0}
    

@routerDenunciado.post('/getById')
async def obtenerDenunciadoById(request:Request):
    try:
        data = await request.json()
        id_denunciado = data.get('id_denunciado')
        denunciado = await getDenunciado(id_denunciado=id_denunciado)
        session.close()
        return denunciado
    except:
        return {"status":0}
    
    

@routerDenunciado.get('/all')
async def alldenunciados():
    denunciados = await listarDenunciados()
    session.close()
    return denunciados

@routerDenunciado.post('/estado')
async def changeEstado(request:Request):
    try:
        data = await request.json()
        id_denunciado = data.get('id_denunciado')
        await cambiarEstado(id_denunciado=id_denunciado)
        session.close()
        return {"status":1}
    except:
        return {"status":0}