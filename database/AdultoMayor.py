# base de datos

from dateutil.parser import parse
from database.conexion import session, engine
from models.AdultoMayor import AdultoMayor


async def insertAdulto(data):
    ci = data.get('ci')
    edad = data.get('edad')
    estado_civil = data.get('estado_civil')
    f_nacimiento = parse(data.get('fecha_nac')).date()
    materno = data.get('materno')
    paterno = data.get('paterno')
    nombre = data.get('nombre')
    nro_referencia = data.get('referencia')
    genero = data.get('sexo')
    beneficios = data.get('beneficios')
    ocupacion = data.get('ocupacion')
    adultoMayor = AdultoMayor(id_adulto=AdultoMayor.generate_id(), ci=ci, edad=edad, estado_civil=estado_civil, f_nacimiento=f_nacimiento,  paterno=paterno,
                              materno=materno,
                              nombre=nombre, nro_referencia=nro_referencia, genero=genero,  beneficios=beneficios,
                              ocupacion=ocupacion)

    session.add(adultoMayor)
    session.commit()
    return adultoMayor.id_adulto


async def listarAdulto():
    adultos = session.query(AdultoMayor).all()
    return adultos


async def getUltimoAdulto():
    return None
