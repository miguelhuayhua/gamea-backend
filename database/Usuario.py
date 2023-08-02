# base de datos
from dateutil.parser import parse
from sqlalchemy import desc
from database.conexion import session
from models.Usuario import Usuario
import os
import bcrypt
async def insertUsuario(data):
    file = data.get('fotografia')
    file_path = os.path.join(file.filename)
    file_path = file_path.replace(' ','')
    file_path = file_path.lower()
    file_path = f'public/userimg/{file_path}'
    with open(file_path, "wb") as f:
        contents = await file.read()
        f.write(contents)
    usuario_name = data.get('usuario')
    password = data.get('password')
    id_persona = data.get('id_persona')
    usuario = Usuario(id_usuario = Usuario.generate_id(), usuario = usuario_name,
                      password = password , fotografia = f"/static/images/{file_path}", 
                      id_persona = id_persona)
    session.add(usuario)
    session.commit()
    return usuario.id_usuario

async def verifyUsuario(usuario):
    result = session.query(Usuario).filter_by(usuario = usuario.get('usuario')).first()
    if(usuario.get('id_usuario')==""):
        return result
    else:
        try:
            usuarioExist = session.query(Usuario).filter_by(id_usuario = usuario.get('id_usuario')).first()
            if(usuarioExist.usuario == result.usuario):
                return None
            else:
                return usuarioExist
        except Exception as e:
            print(e)
    


async def listarUsuarios():
    return session.query(Usuario).order_by(desc(Usuario.id_usuario)).all()



async def getUsuario(id_usuario)->Usuario:
    usuario = session.query(Usuario).filter_by(id_usuario = id_usuario).first()
    return usuario


async def cambiarEstado(id_usuario):
    usuario = session.query(Usuario).filter_by(id_usuario = id_usuario).first()
    if usuario.estado ==0:
        usuario.estado = 1
    else :
        usuario.estado= 0
    session.commit()
    return True

async def modificarUsuario(usuario):
    id_usuario = usuario.get('id_usuario')
    usuarioUpdated = session.query(Usuario).filter_by(id_usuario = id_usuario).first()
    file = usuario.get('fotografia')
    if(file != 'null'):
        file_path = os.path.join(file.filename)
        file_path = file_path.replace(' ','')
        file_path = file_path.lower()
        print(file_path)
        with open('public/usersimg/'+file.filename, "wb") as f:
            contents = await file.read()
            f.write(contents)
        usuarioUpdated.fotografia = f"/static/images/{file_path}", 
    if(usuario.get('password')!=''):
        usuarioUpdated.password = usuario.get('password')
    usuarioUpdated.usuario = usuario.get('usuario')
    session.commit()
    return usuarioUpdated.id_usuario
 
async def getByNameAndPassword(usuario):    
    
    usuario_name = usuario.get('usuario')
    password = usuario.get('password')
    result = None
    if(usuario_name and password):
        b_password = password.encode('utf-8')
        result = session.query(Usuario).filter_by(usuario = usuario_name).first()
        
        if bcrypt.checkpw(b_password,result.password.encode('utf-8')):
            result.password = None
            return result
        else: 
        
            return None
    else:
        return None