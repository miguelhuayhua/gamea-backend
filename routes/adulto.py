from database.AdultoMayor import all, insert
from models.AdultoMayor import AdultoMayor
from fastapi import APIRouter

router = APIRouter()


# creamos las diferentes rutas de manejo para cada caso


@router.get('/all')
async def allAdulto():
    return await all()


@router.post('/insert')
async def insertAdulto(adultoMayor: AdultoMayor):
    return adultoMayor.dict()
