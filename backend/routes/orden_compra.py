from fastapi import APIRouter, HTTPException, status
from sqlalchemy import or_,update
from typing import List
from database import db_dependency
from models.productos import *
from models.ventas import *

router = APIRouter(prefix="/orden_compra")

@router.post("/crear", status_code=status.HTTP_201_CREATED)
async def nueva_orden(request: nueva_orden, db: db_dependency):
    if(request):
        received = Orden_Compra(**request.model_dump())
        try:
            db.add(received)
        except:
            raise HTTPException(status_code=442, detail='Orden de Compra no pudo ser creada') 
        db.commit()       
        response = db.query(Orden_Compra).order_by(Orden_Compra.orden_compra_id.desc()).first()
        return {    "cliente_id": response.cliente_id,
                    "vendedor_id":response.vendedor_id,
                    "fecha": response.fecha,
                    "direccion": response.direccion,
                    "metodo_despacho": response.metodo_despacho} 
    else:
        raise HTTPException(status_code=400, detail='No se ingreso orden de compra valida')

@router.get("/",status_code=status.HTTP_200_OK)
async def lista(db: db_dependency):
    response = db.query(Orden_Compra).all() 
    return response
    
@router.put("/metodo_despacho",status_code=status.HTTP_200_OK)   
async def metodo_despacho(request: metodo_despacho, db: db_dependency):
    statement = (update(Orden_Compra).where(Orden_Compra.orden_compra_id == request.orden_compra_id)).values(metodo_despacho = request.metodo_despacho)
    db.execute(statement)
    db.commit()
    response = db.query(Orden_Compra).filter(Orden_Compra.orden_compra_id == request.orden_compra_id).first()
    return response.metodo_despacho

@router.put("/direccion",status_code=status.HTTP_200_OK)
async def metodo_despacho(request: direccion_despacho, db: db_dependency):
    statement = (update(Orden_Compra).where(Orden_Compra.orden_compra_id == request.orden_compra_id)).values(direccion = request.direccion)
    db.execute(statement)
    db.commit()
    response = db.query(Orden_Compra).filter(Orden_Compra.orden_compra_id == request.orden_compra_id).first()
    return response.direccion