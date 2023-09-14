
import tempfile

from fastapi.responses import FileResponse
from database.Usuario import insertUsuario, verifyUsuario, cambiarEstado, listarUsuarios, modificarUsuario,getUsuario, getByNameAndPassword
from fastapi import APIRouter, Request
import pandas as pd
from database.conexion import session
routerUsuario = APIRouter()


# creamos las diferentes rutas de manejo para cada usuario





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
    usuarios_json = [usuario.__dict__ for usuario in usuarios]
    for usuario_json in usuarios_json:
        if 'password' in usuario_json:
            del usuario_json['password']
    session.close()
    return usuarios_json

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


           
@routerUsuario.get('/report')
async def reportUsuario():
    dataUsuarios = await listarUsuarios()
    usuarios = []
    for usuario in dataUsuarios:
        dict = usuario.__dict__
        dict.pop('_sa_instance_state')
        usuarios.append(dict)
    dataframeUsuarios = pd.DataFrame.from_records(usuarios)
    del dataframeUsuarios['password']
    dataframeUsuarios['ult_modificacion'] = dataframeUsuarios['ult_modificacion'].dt.strftime('%Y-%m-%d %H:%M:%S')    
    
      # Crea un archivo temporal
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        # Guarda el DataFrame en el archivo temporal en formato Excel
        dataframeUsuarios.to_excel(temp_file.name, sheet_name='usuarios', index=False, engine='xlsxwriter')

    # Envía el archivo como respuesta utilizando FileResponse
    return FileResponse(temp_file.name, filename='archivo.xlsx')
