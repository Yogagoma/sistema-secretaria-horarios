from fastapi import FastAPI
from models.base import Base

Base.metadata.create_all()

# Inicializar servidor fastAPI
app = FastAPI()