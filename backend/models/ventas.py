from database import mysql_database
from datetime import date, datetime, time, timedelta
from pydantic import BaseModel

Cliente = mysql_database.classes.clientes
Vendedor = mysql_database.classes.vendedores

#------------Ordenes y pagos------------
Orden_Compra = mysql_database.classes.orden_compra
Pago = mysql_database.classes.pagos

class nueva_orden(BaseModel):
    cliente_id: int
    vendedor_id: int
    fecha: datetime
    direccion: str
    metodo_despacho: str

class orden_compra_fitro(BaseModel):
    orden_compra_id: int
    rut_cliente: int
    rut_vendedor: int
    fecha: datetime

class metodo_despacho(BaseModel):
    orden_compra_id: int
    metodo_despacho: str

class direccion_despacho(BaseModel):
    orden_compra_id: int
    direccion: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "orden_compra_id": 1,
                    "direccion": "direcion_actualizada"
                }
            ]
        }
    }

#------------Pedidos------------
Pedido = mysql_database.classes.pedidos

class nuevo_pedido(BaseModel):
    SKU: str
    cantidad: int
    orden_compra_id: int
    estado: str

class pedidos_filtro(BaseModel):
    pedido_id: int
    orden_compra_id: int
    sku: str

class aceptar_pedido(BaseModel):
    pedido_id: int