from database.Denunciado import getDenunciadoByCaso

from fastapi import APIRouter, Request
from database.conexion import session
routerDenunciado = APIRouter()



@routerDenunciado.post('/obtener')
async def obtenerDenunciado(request:Request):
    try:
        data = await request.json()
        id_caso = data.get('id_caso')
        denunciado = await getDenunciadoByCaso(id_caso=id_caso)
        session.close()
        return denunciado
    except:
        return {"status":0}