from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# importamos todas las rutas que creamos en la carpeta "routes"
from routes.adulto import routerAdulto
from routes.denuncia import routerDenuncia
from routes.caso import routerCaso
from routes.denunciado import routerDenunciado
from routes.domicilio import routerDomicilio
from routes.hijo import routerHijo
app = FastAPI()


origins = [
    "http://localhost:3000",
    "http://localhost:8080",
    "https://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# colocado de las rutas en la aplicación principal
app.include_router(routerAdulto, prefix='/adulto')
app.include_router(routerDenuncia, prefix='/denuncia')
app.include_router(routerCaso, prefix='/caso')
app.include_router(routerDenunciado, prefix='/denunciado')
app.include_router(routerDomicilio, prefix='/domicilio')
app.include_router(routerHijo, prefix='/hijo')
