from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.base import Base

Base.metadata.create_all()

# Inicializar servidor fastAPI
app = FastAPI()

# Agregar el middleware del sistema
app.add_middleware(
    CORSMiddleware, # Habilita el Intercambio de Recursos de Origen Cruzado(CORS)
    allow_origins=["http://localhost:8000"], # Especifica la ruta y el puerto 8000
    allow_methods= ["*"] # Permite todos los métodos del backend
)
