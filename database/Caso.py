# base de datos

from dateutil.parser import parse
from database.conexion import session
from models.Caso import Caso
from sqlalchemy import desc

async def insertCaso(data, id_adulto):
    fecha_registro = data.get('fecha')
    tipologia = data.get('tipologia')
    year = parse(fecha_registro).year
    hora_registro = data.get('hora')
    nro_caso = str(data.get('nro_caso')) + "/"+str(year)
    descripcion_hechos = data.get('descripcion_hechos')
    peticion = data.get('peticion')
    accion_realizada = data.get('accion_realizada')
    caso = Caso(id_caso=Caso.generate_id(),
                fecha_registro=fecha_registro,
                hora_registro=hora_registro,
                tipologia=tipologia,
                nro_caso=nro_caso,
                descripcion_hechos=descripcion_hechos,
                peticion=peticion,
                accion_realizada=accion_realizada,
                id_adulto=id_adulto)
    session.add(caso)
    session.commit()
    return caso.id_caso


async def getUltimoCaso():
    return session.query(Caso).order_by(desc(Caso.id_caso)).first()

async def allCasos():
    return session.query(Caso).order_by(Caso.id_caso).all()

async def cambiarEstado(id_caso):
    caso = session.query(Caso).filter_by(id_caso = id_caso).first()
    if caso.estado ==0:
        caso.estado = 1
    else :
        caso.estado= 0
    session.commit()
    return True


async def modificarCaso(caso):
    try:
        print(caso.get('descripcion_hechos'))
        print(caso.get('id_caso'))
        casoUpdated = session.query(Caso).filter_by(id_caso=caso.get('id_caso')).first()
        casoUpdated.descripcion_hechos = caso.get('descripcion_hechos')
        casoUpdated.peticion = caso.get('peticion')
        casoUpdated.accion_realizada = caso.get('accion_realizada')
        session.commit()
        return True
    except:
        return False


    