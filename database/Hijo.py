# base de datos

from dateutil.parser import parse
from database.conexion import session
from models.Hijo import Hijo


async def insertHijo(hijos, id_adulto):
    for nombre_apellidos in hijos:
        hijo = Hijo(id_hijo=Hijo.generate_id(),
                    nombres_apellidos=nombre_apellidos.strip(),
                    id_adulto=id_adulto
                    )
        session.add(hijo)
    session.commit()
    return len(hijos)

async def getHijosByIdAdulto(id_adulto):
    hijos = session.query(Hijo).filter_by(id_adulto=id_adulto).all()
    return hijos


async def listarHijos():
    return session.query(Hijo).all()