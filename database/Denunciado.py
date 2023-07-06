# base de datos

from database.conexion import session, engine
from models.Denunciado import Denunciado


async def insertDenunciado(data, id_caso):
    materno = data.get('materno')
    paterno = data.get('paterno')
    nombres = data.get('nombres')
    parentezco = data.get('parentezco')
    denunciado = Denunciado(id_denunciado=Denunciado.generate_id(), paterno=paterno,
                            materno=materno,
                            nombres=nombres,
                            parentezco=parentezco,
                            id_caso=id_caso)

    session.add(denunciado)
    session.commit()
    return denunciado.id_denunciado


async def listar():
    return None
