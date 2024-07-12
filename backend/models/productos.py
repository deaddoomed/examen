from database import mysql_database
from pydantic import BaseModel

#------------Productos------------
Producto = mysql_database.classes.productos
Categoria = mysql_database.classes.categorias

class productos_filtro(BaseModel):
    sku: str
    codigo: str
    categoria: str
    nombre: str
    marca: str
    precio_max: int
    precio_min: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "sku": "",
                    "codigo": "",
                    "categoria": "Taladros",
                    "nombre": "",
                    "marca": "",
                    "precio_max": 999999,
                    "precio_min": 0
                }
            ]
        }
    }

class producto_sku(BaseModel):
    sku: str