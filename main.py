from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# importamos todas las rutas que creamos en la carpeta "routes"
from routes.adulto import routerAdulto
from routes.denuncia import routerDenuncia
app = FastAPI()


origins = [
    "http://localhost:3000",
    "http://localhost:8080",
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
