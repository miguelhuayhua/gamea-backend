# base de datos
from datetime import date
from dateutil.parser import parse
from database.conexion import session, engine
from models.Domicilio import Domicilio


async def insertDomicilio(data, id_adulto):
    distrito = data.get('distrito')
    zona = data.get('zona')
    calle_av = data.get('calle_av')
    nro_vivienda = data.get('nro_vivienda')
    area = data.get('area')
    otra_area = data.get('otra_area')
    domicilio = Domicilio(id_domicilio=Domicilio.generate_id(),
                          distrito=distrito,
                          zona=zona,
                          calle_av=calle_av,
                          nro_vivienda=nro_vivienda,
                          area=area,
                          otra_area=otra_area,
                          id_adulto=id_adulto)
    session.add(domicilio)
    session.commit()
    return domicilio.id_domicilio


async def listarDomicilio():
    return session.query(Domicilio).all()
