from database.AdultoMayor import insertAdulto
from fastapi import APIRouter, Request

routerDenuncia = APIRouter()
# funciones de modelos de la base de datos

# creamos las diferentes rutas de manejo para cada caso


@routerDenuncia.post('/insert')
async def insertDenuncia(request: Request):
    try:
        data = await request.json()
        datosGenerales = data.get('datosGenerales')
        await insertAdulto(datosGenerales)
        datosUbicacion = data.get('datosUbicacion')
        datosDenunciado = data.get('datosDenunciado')
        descripcionHechos = data.get('descripcionHechos')
        descripcionPeticion = data.get('descripcionPeticion')
        accionesRealizadas = data.get('accionesRealizadas')
        datosDenuncia = data.get('datosDenuncia')
        return {"response": "Los datos se han registrado correctamente..."}

    except Exception as e:
        print(e)
        return {"response": "Ha ocurrido un error en el servidor..."}
