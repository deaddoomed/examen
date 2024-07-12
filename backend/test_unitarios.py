from sqlalchemy import text
from database import SessionLocal
from models.productos import *
from models.ventas import *

session = SessionLocal()

def test_base_datos_conexion():
    rs = session.execute(text('SELECT 1')).mappings().all()
    session.close()
    assert rs[0]['1'] == 1

def test_base_datos_select_desde_tabla():
    rs = session.execute(text('SELECT * from ferremas.orden_compra LIMIT 1')).mappings().all()
    session.close()
    assert rs[0]['orden_compra_id'] == 1

def test_base_datos_orm_conexion():
    try:
        rs = session.query(Orden_Compra).first()
        resultado = True
    except:
        resultado = False
    session.close()
    assert resultado == True

def test_base_datos_orm_conexion_filtro_invalido():
    try:
        rs = session.query(Orden_Compra).filter(Orden_Compra.orden_compra_id == 0).first()
        resultado = rs
    except:
        resultado = False
    session.close()
    assert resultado == None