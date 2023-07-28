
from database.Usuario import insertUsuario, verifyUsuario, cambiarEstado, listarUsuarios, modificarUsuario,getUsuario
from fastapi import APIRouter, Request
import pandas as pd
from database.conexion import session
routerUsuario = APIRouter()


# creamos las diferentes rutas de manejo para cada caso





@routerUsuario.post('/verify')
async def obtenerusuario(request: Request):
    data = await request.json()
    nombre_usuario = data.get('usuario')
    if await verifyUsuario(nombre_usuario):
        return {"status":0}
    else:
        return {"status":1}
    


@routerUsuario.get('/all')
async def allusuarios():
    usuarios = await listarUsuarios()
    session.close()
    return usuarios

@routerUsuario.post('/estado')
async def changeEstado(request:Request):
    try:
        data = await request.json()
        id_usuario = data.get('id_usuario')
        await cambiarEstado(id_usuario=id_usuario)
        session.close()
        return {"status":1}
    except:
        return {"status":0}
    


@routerUsuario.post('/update')
async def updateusuario(request:Request):
    try:
        usuario = await request.json()
        await modificarUsuario(usuario = usuario)
        session.close()
        return {"status":1}
    except Exception as e:
        print(e)
        return {"status":0}
    


@routerUsuario.post('/insert')
async def insertarUsuario(request:Request):
    try:
        usuario = await request.form()
        await insertUsuario(data=  usuario)
        session.close()
        return {"status":1}
    except Exception as e:
        print(e)
        return {"status":0}