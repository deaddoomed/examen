from fastapi.testclient import TestClient
import json
from main import app

client = TestClient(app)
    
def test_server_running_exito():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "API is running"

# ORDEN COMPRA /////////////////////////////////////////////////////////////////////
    
def test_orden_compra_crear_listar_ordenes():
    response = client.get("/orden_compra/")
    assert response.status_code == 200

# ORDEN COMPRA    
def test_orden_compra_crear_nuevo_dato_valido():
    request = { "cliente_id": 1,
                "vendedor_id": 1,
                "fecha": "2024-06-21T19:14:39",
                "direccion": "direccion_nuevo",
                "metodo_despacho": "metodo_despacho_nuevo"}
    response = client.post("/orden_compra/crear", content = json.dumps(request))
    assert response.status_code == 201
    assert response.json() == request

def test_orden_compra_crear_nuevo_campo_faltante():
    request = { "cliente_id": 1,
                "vendedor_id": 1,
                "fecha": "2024-06-21T19:14:39",
                "metodo_despacho": "direccion_faltante"}
    response = client.post("/orden_compra/crear", content = json.dumps(request))
    assert response.status_code == 422

def test_orden_compra_crear_nuevo_dato_invalido():
    request = { "cliente_id": 1,
                "vendedor_id": 1,
                "fecha": "2024-06-21T19:14:39",
                "direccion": 1000,
                "metodo_despacho": "direccion_faltante"}
    response = client.post("/orden_compra/crear", content = json.dumps(request))
    assert response.status_code == 422

def test_orden_compra_crear_nuevo_dato_extra():
    request = { "cliente_id": 1,
                "vendedor_id": 1,
                "fecha": "2024-06-21T19:14:39",
                "direccion": "direccion_nuevo",
                "metodo_despacho": "direccion_faltante",
                "campo_extra": "valor_extra"}
    response = client.post("/orden_compra/crear", content = json.dumps(request))
    assert response.status_code == 422

def test_orden_compra_crear_nuevo_vacio():
    request = { }
    response = client.post("/orden_compra/crear", content = json.dumps(request))
    assert response.status_code == 422


# DIRECCION
def test_orden_compra_cambio_direccion_dato_valido():
    request = { "orden_compra_id": 1,"direccion": "direccion_actualizada" }
    response = client.put("/orden_compra/direccion", content = json.dumps(request))
    assert response.status_code == 200
    assert response.json() == "direccion_actualizada"

def test_orden_compra_cambio_direccion_fallido_dato_vacio():
    request = { }
    response = client.put("/orden_compra/direccion", content = json.dumps(request))
    assert response.status_code == 422

def test_orden_compra_cambio_direccion_fallido_dato_invalido():
    request = { "orden_compra_id": 1,"direccion": 1000 }
    response = client.put("/orden_compra/direccion", content = json.dumps(request))
    assert response.status_code == 422

# METODO DE DESPACHO
def test_orden_compra_cambio_metodo_despacho_dato_valido():
    request = { "orden_compra_id": 1,"metodo_despacho": "metodo_despacho_actualizado" }
    response = client.put("/orden_compra/metodo_despacho", content = json.dumps(request))
    assert response.status_code == 200
    assert response.json() == "metodo_despacho_actualizado"

def test_orden_compra_cambio_metodo_despacho_fallido_dato_vacio():
    request = { }
    response = client.put("/orden_compra/metodo_despacho", content = json.dumps(request))
    assert response.status_code == 422

def test_orden_compra_cambio_metodo_despacho_fallido_dato_invalido():
    request = { "orden_compra_id": 1,"metodo_despacho": 1000 }
    response = client.put("/orden_compra/metodo_despacho", content = json.dumps(request))
    assert response.status_code == 422