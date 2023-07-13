# base de datos

from dateutil.parser import parse
from fastapi import Request
from database.conexion import session, engine
from models.AdultoMayor import AdultoMayor
from models.Hijo import Hijo
from sqlalchemy.orm import joinedload

from sqlalchemy import and_ ,not_
async def insertAdulto(data):
    ci = data.get('ci')
    edad = data.get('edad')
    estado_civil = data.get('estado_civil')
    f_nacimiento = parse(data.get('fecha_nac')).date()
    materno = data.get('materno').strip().capitalize()
    paterno = data.get('paterno').strip().capitalize()
    nombre = data.get('nombre').strip().capitalize()
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

async def getAdulto(id_adulto)->AdultoMayor:
    adulto = session.query(AdultoMayor).filter_by(id_adulto = id_adulto).first()
    return adulto