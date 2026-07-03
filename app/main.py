from fastapi import FastAPI, HTTPException, status
from .Enrutadores.clintes import ruta_cliente
from .Enrutadores.facturas import ruta_facturas
from .Enrutadores.transacciones import ruta_transacciones
from .conexion_base_d import crear_tablas

app= FastAPI (lifespan= crear_tablas)

#incluir ruta de clientes 
app.include_router(ruta_cliente, tags=["Clientes"])
app.include_router(ruta_facturas, tags=["Facturas"])
app.include_router(ruta_transacciones, tags=["Transacciones"])
