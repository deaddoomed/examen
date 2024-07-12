from database import mysql_database
from datetime import date, datetime, time, timedelta
from pydantic import BaseModel

#------------Despachos------------
Despacho = mysql_database.classes.despachos

class nuevo_despacho(BaseModel):
    pedido_id: int
    fecha: datetime
    cantidad: int

class despacho_filtro(BaseModel):
    despacho_id: int
    pedido_id: int
