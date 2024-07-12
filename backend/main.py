from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from routes import productos, pedidos, despachos, orden_compra, login
from datetime import datetime, timedelta, timezone

app = FastAPI()

#-----routes-----
app.include_router(productos.router)
app.include_router(pedidos.router)
app.include_router(despachos.router)
app.include_router(orden_compra.router)
app.include_router(login.router)


origins = [
    "http://localhost",
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", status_code=status.HTTP_200_OK)
async def testing():
    return "API is running"

