from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app=FastAPI()

class alumno(BaseModel):
    nc:int
    hacks:int 
    inicio:str
    fin:Optional[str]
    password:str


#127.0.0.1:8000
@app.get("/")
def index():
    return {"message":"Hola raspberry"}
@app.get("/alumnos/{id}")
def mostrar_alumnos(id:int):
    return {"data":id}
@app.post("/alumnos")
def instar_alumno(alumno:alumno):
    return {"message": f"{alumno.nc} insertado"}