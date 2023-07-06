# base de datos
from database.conexion import database
from datetime import date


async def insertAdulto(data):
    ci = data.get('ci')
    edad = data.get('edad')
    estado_civil = data.get('estado_civil')
    fecha_nac = data.get('fecha_nac')
    materno = data.get('materno')
    paterno = data.get('paterno')
    nombre = data.get('nombre')
    referencia = data.get('referencia')
    genero = data.get('sexo')
    grado = data.get('grado')
    beneficios = data.get('beneficios')
    ocupacion = data.get('ocupacion')
    await database.execute(
        query="""INSERT INTO adulto_mayor (nombre, paterno, materno, edad, ci, genero, f_nacimiento, estado_civil, nro_referencia, ocupacion, beneficios)
          VALUES (:nombre, :paterno, :materno, :edad, :ci, :genero, :fecha_nac , :estado_civil, :referencia, :ocupacion, :beneficios ) """,
        values={'nombre': nombre, 'paterno': paterno, 'materno': materno, 'edad': edad, 'ci': ci, 'genero': genero,
                'fecha_nac': date.fromisoformat(fecha_nac), 'estado_civil': estado_civil, 'referencia': referencia, 'ocupacion': ocupacion, 'beneficios': beneficios})
    database.force_rollback()


async def listar():
    datos = await database.fetch_all('SELECT * FROM adulto_mayor')
    return datos
