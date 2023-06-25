from pydantic import BaseModel, Field
from datetime import date, datetime


class AdultoMayor(BaseModel):
    id: str = None
    nombre: str
    paterno: str
    materno: str
    edad: int
    ci: int
    genero: str
    f_nacimiento: date
    estado_civil: str
    nro_referencia: int
    ocupacion: str
    beneficios: str
    estado: int = Field(default_factory=1, alias="estado")
    ult_modificacion: datetime 
