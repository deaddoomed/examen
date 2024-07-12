from database import mysql_database
from pydantic import BaseModel

Usuario = mysql_database.classes.usuarios

class nuevo_usuario(BaseModel):
    nombre: str
    contrasena: str
    email: str

class login(BaseModel):
    usuario: str
    contrasena: str
