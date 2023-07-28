# base de datos
from dateutil.parser import parse
from sqlalchemy import desc
from database.conexion import session
from models.Usuario import Usuario
import os

async def insertUsuario(data):
    file = data.get('fotografia')
    file_path = os.path.join(file.filename)
    file_path = file_path.replace(' ','')
    file_path = file_path.lower()
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
    result = session.query(Usuario).filter_by(usuario = usuario).first()
    return result
    


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
    nombres = usuario.get('nombres')
    paterno = usuario.get('paterno')
    materno = usuario.get('materno')
    ci = usuario.get('ci')
    celular = usuario.get('celular')
    f_nacimiento = usuario.get('f_nacimiento')
    cargo = usuario.get('cargo')
    genero = usuario.get('genero')
    usuarioUpdated = session.query(Usuario).filter_by(id_usuario  = usuario.get('id_usuario')).first()
    usuarioUpdated.nombres = nombres,
    usuarioUpdated.paterno = paterno
    usuarioUpdated.materno = materno
    usuarioUpdated.ci = ci
    usuarioUpdated.celular = celular
    usuarioUpdated.f_nacimiento = f_nacimiento 
    usuarioUpdated.cargo = cargo
    session.commit()
    return usuarioUpdated.id_usuario
 
