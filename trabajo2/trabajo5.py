# https://github.com/viniesqui/mdd_lead.git

from typing import List
from fastapi import FastAPI, Depends
from pydantic import BaseModel


class Usuario(BaseModel):
    id: int
    username: str
    email: str
    password: str


class Tarea(BaseModel):
    id: int
    title: str
    description: str
    status: str
    user_id: int


class AlmacenDatos:
    def __init__(self):
        self.usuarios = []
        self.tareas = []


app = FastAPI()


def obtener_almacen_datos():
    return AlmacenDatos()


@app.post("/registro")
def registrar_usuario(usuario: Usuario, almacen_datos: AlmacenDatos = Depends(obtener_almacen_datos)):
    almacen_datos.usuarios.append(usuario)
    return {"mensaje": "Usuario registrado exitosamente"}


@app.get("/usuario/{id}")
def obtener_usuario(id: int, almacen_datos: AlmacenDatos = Depends(obtener_almacen_datos)):
    for usuario in almacen_datos.usuarios:
        if usuario.id == id:
            return usuario
    return {"mensaje": "Usuario no encontrado"}


@app.post("/tareas/crear")
def crear_tarea(tarea: Tarea, almacen_datos: AlmacenDatos = Depends(obtener_almacen_datos)):
    almacen_datos.tareas.append(tarea)
    return {"mensaje": "Tarea creada exitosamente"}


@app.get("/tareas/{user_id}")
def obtener_tareas(user_id: int, almacen_datos: AlmacenDatos = Depends(obtener_almacen_datos)):
    tareas_usuario = [
        tarea for tarea in almacen_datos.tareas if tarea.user_id == user_id]
    return tareas_usuario
