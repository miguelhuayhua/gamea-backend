
from database.Usuario import insertUsuario, verifyUsuario, cambiarEstado, listarUsuarios, modificarUsuario,getUsuario, getByNameAndPassword
from fastapi import APIRouter, Request
import pandas as pd
from database.conexion import session
routerUsuario = APIRouter()


# creamos las diferentes rutas de manejo para cada caso





@routerUsuario.post('/verify')
async def obtenerusuario(request: Request):
    data = await request.json()
    if await verifyUsuario(usuario = data):
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
        usuario = await request.form()
        await modificarUsuario(usuario = usuario)
        session.close()
        return {"status":1}
    except Exception as e:
        print(e)
        return {"status":0}
    
@routerUsuario.post('/get')
async def obtenerUsuario(request: Request):
    data = await request.json()
    id_usuario  = data.get('id_usuario')
    usuario = await getUsuario(id_usuario= id_usuario)
    return usuario

@routerUsuario.post('/auth')
async def authUsuario(request: Request):
    data = await request.json()
    usuario = await getByNameAndPassword(data)
    return usuario


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