from fastapi import APIRouter, HTTPException, status
from sqlalchemy import or_,update
from typing import List
from database import db_dependency
from models.productos import *
from models.ventas import *

router = APIRouter(prefix="/pedidos")

@router.post("/ingresar", status_code=status.HTTP_201_CREATED)
async def nuevo_pedido(requests: List[nuevo_pedido], db: db_dependency):
    if(requests):
        for request in requests:
            received = Pedido(**request.model_dump())
            try:
                db.add(received)
            except:
                raise HTTPException(status_code=442, detail='Pedido no pudo ser creado') 
        db.commit()       
        return "Pedido creado!"
    else:
        raise HTTPException(status_code=401, detail='No se ingreso pedido valido')

@router.post("/busqueda",status_code=status.HTTP_200_OK)
async def busqueda(request: pedidos_filtro, db: db_dependency):
    if(request):
        response = []
        pedidos = db.query(Pedido).filter(or_(  Pedido.pedido_id == request.pedido_id,
                                                Pedido.SKU == request.sku,
                                                Pedido.orden_compra_id == request.orden_compra_id)).all()
        for pedido in pedidos:
            producto = db.query(Producto).filter(Producto.SKU == pedido.SKU).first()
            orden_compra = db.query(Orden_Compra).filter(Orden_Compra.orden_compra_id == pedido.orden_compra_id).first()

            precio_pedido = producto.precio * pedido.cantidad

            if(pedido and producto):  
                append_to = {   'Codigo Pedido': pedido.pedido_id,
                                'Orden de Compra': pedido.orden_compra_id,
                                'Fecha': orden_compra.fecha,
                                'Detalle':{ 'SKU': pedido.SKU,
                                            'Produto': producto.nombre,
                                            'Cantidad': pedido.cantidad,
                                            'Precio Unitario': producto.precio,
                                            'Precio Total': precio_pedido,
                                            'Estado': pedido.estado}
                            }
                response.append(append_to)
 
        return response
    else:
        raise HTTPException(status_code=401, detail='Invalid Request Data: Filter information is invalid')
    
@router.put("/aceptar",status_code=status.HTTP_200_OK)
async def aceptar_pedidos(request: aceptar_pedido, db: db_dependency):
    statement = (update(Pedido).where(Pedido.pedido_id == request.pedido_id)).values(estado = 'aceptado')
    db.execute(statement)
    db.commit()
    response = db.query(Pedido).filter(Pedido.pedido_id == request.pedido_id).first()
    return response

@router.put("/rechazar",status_code=status.HTTP_200_OK)
async def rechazar_pedidos(request: aceptar_pedido, db: db_dependency):
    statement = (update(Pedido).where(Pedido.pedido_id == request.pedido_id)).values(estado = 'rechazado')
    db.execute(statement)
    db.commit()
    response = db.query(Pedido).filter(Pedido.pedido_id == request.pedido_id).first()
    return response.estado