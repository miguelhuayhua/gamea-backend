# base de datos

from database.conexion import session, engine
from models.Denunciado import Denunciado


async def insertDenunciado(data, id_caso):
    materno = data.get('materno').strip()
    paterno = data.get('paterno').strip()
    nombres = data.get('nombres').strip()
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


async def getDenunciadoByCaso(id_caso)->Denunciado:
    denunciado = session.query(Denunciado).filter_by(id_caso = id_caso).first()
    return denunciado
