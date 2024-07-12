from fastapi import APIRouter, HTTPException, status
from sqlalchemy import or_,update
from typing import List
from database import db_dependency
from models.productos import *
from models.bodega import *
from models.ventas import *

router = APIRouter(prefix="/despachos")

@router.post("/ingresar", status_code=status.HTTP_201_CREATED)
async def nuevo_pedido(request: nuevo_despacho, db: db_dependency):
    if(request):
        received = Despacho(**request.model_dump())
        try:
            db.add(received)
            pedido = db.query(Pedido).filter(Pedido.pedido_id == received.pedido_id).first()
            producto = db.query(Producto).filter(Producto.SKU == pedido.SKU).first()
            stock_nuevo = producto.stock - received.cantidad
            statement = (update(Producto).where(Producto.SKU == pedido.SKU)).values(stock = stock_nuevo)
            db.execute(statement)
        except:
            raise HTTPException(status_code=442, detail='Despacho no pudo ser ingresado') 
        db.commit()       
        return "Despacho ingresado!"
    else:
        raise HTTPException(status_code=401, detail='No se ingreso despacho valido')

@router.post("/busqueda",status_code=status.HTTP_200_OK)
async def busqueda(request: despacho_filtro, db: db_dependency):
    if(request):
        response = []
        despachos = db.query(Despacho).filter(or_(Despacho.despacho_id == request.despacho_id,
                                                Despacho.pedido_id == request.pedido_id,)).all()
        for despacho in despachos:            
            pedido = db.query(Pedido).filter(Pedido.pedido_id == despacho.pedido_id).first()
            producto = db.query(Producto).filter(Producto.SKU == pedido.SKU).first()

            if(despacho and producto and pedido):  
                append_to = {   'Codigo Despacho': despacho.despacho_id,
                                'Fecha de Despacho': despacho.fecha,
                                'Detalles':{'Orden de Compra': pedido.orden_compra_id,
                                            'Codigo Pedido': despacho.pedido_id,
                                            'SKU': pedido.SKU,
                                            'Produto': producto.nombre,
                                            'Cantidad Solicitada': pedido.cantidad,
                                            'Cantidad Despacho': despacho.cantidad}
                            }
                response.append(append_to)
 
        return response
    else:
        raise HTTPException(status_code=401, detail='Invalid Request Data: Filter information is invalid')