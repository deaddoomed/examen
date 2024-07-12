from fastapi import APIRouter, HTTPException, status
from sqlalchemy import or_,update
from database import db_dependency
from models.productos import *

router = APIRouter(prefix="/productos")

@router.get("/",status_code=status.HTTP_200_OK)
async def lista(db: db_dependency):
    productos = db.query(Producto).all() 
    return productos
   
@router.post("/busqueda",status_code=status.HTTP_200_OK)
async def busqueda(request: productos_filtro, db: db_dependency):
    if(request):
        response = []
        productos = db.query(Producto).filter(  Producto.SKU.like('%'+request.sku+'%'),
                                                Producto.codigo.like('%'+request.codigo+'%'),
                                                Producto.nombre.like('%'+request.nombre+'%'),
                                                Producto.marca.like('%'+request.marca+'%'),
                                                Producto.precio.between(request.precio_min,request.precio_max),
                                                Producto.stock > 0).all()
        for producto in productos:
            categoria = db.query(Categoria).filter(Categoria.categoria.like('%'+request.categoria+'%'),
                                                   Categoria.categoria_id == producto.categoria_id).first()
            if(producto and categoria):  
                append_to = {   'SKU': producto.SKU,
                                'Codigo Producto': producto.codigo,
                                'Categoria': categoria.categoria,
                                'Producto':producto.nombre,
                                'Marca': producto.marca,
                                'Precio': producto.precio,
                                'Stock': producto.stock
                            }
                response.append(append_to)
 
        return response
    else:
        raise HTTPException(status_code=401, detail='Invalid Request Data: Filter information is invalid')
    
@router.post("/disponibilidad",status_code=status.HTTP_200_OK)
async def busqueda(request: producto_sku, db: db_dependency):
    if(request):
        producto = db.query(Producto).filter(Producto.SKU == request.sku).first()

        response = {    'sku' : producto.SKU,
                        'producto' : producto.nombre,
                        'stock' : producto.stock
                    }
    
        return request
    else:
        raise HTTPException(status_code=401, detail='Invalid Request Data: Filter information is invalid')