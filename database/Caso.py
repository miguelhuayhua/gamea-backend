# base de datos

from dateutil.parser import parse
from database.conexion import session
from models.Caso import Caso


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
