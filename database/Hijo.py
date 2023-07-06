# base de datos

from dateutil.parser import parse
from database.conexion import session
from models.Hijo import Hijo


async def insertHijo(hijos, id_adulto):
    for nombre_apellidos in hijos:
        hijo = Hijo(id_hijo=Hijo.generate_id(),
                    nombres_apellidos=nombre_apellidos,
                    id_adulto=id_adulto
                    )
        session.add(hijo)
    session.commit()
    return len(hijos)
