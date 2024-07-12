from fastapi import APIRouter, HTTPException, status
from sqlalchemy import or_,update
from database import db_dependency
from models.usuario import *
import bcrypt

router = APIRouter(prefix="/login")

@router.post("/crear", status_code=status.HTTP_201_CREATED)
async def crear_usuario(request: nuevo_usuario, db: db_dependency):
    usuario_nuevo  = Usuario(**request.model_dump())
    if(usuario_nuevo):
        contrasena_encriptada = bcrypt.hashpw(usuario_nuevo.contrasena.encode('utf-8'),bcrypt.gensalt())
        usuario_nuevo.contrasena = contrasena_encriptada
        db.add(usuario_nuevo)
        db.commit()
        return "Usuario Creado"
    else:
        raise HTTPException(status_code=401, detail='Datos de usuario invalidos')
    
@router.post("/",status_code=status.HTTP_200_OK)
async def validar_usuario(datos_login: login, db: db_dependency):
    login_usuario = login(**datos_login.model_dump())
    usuario = db.query(Usuario).filter(or_(Usuario.nombre == login_usuario.usuario, Usuario.email == login_usuario.usuario)).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail='Usuario no existe')
    else:
        if  bcrypt.checkpw(bytes(login_usuario.contrasena,'utf-8'), bytes(usuario.contrasena,'utf-8')):          
            return True
        else:
            raise HTTPException(status_code=401, detail='Contrasena invalida')