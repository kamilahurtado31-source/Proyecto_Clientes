from fastapi import FastAPI

mi_app= FastAPI ()
@mi_app.get ("/mensaje")

def proyecto  ():
    return{"proyecto": "este es el proyecto de clientes a desarrollar"}


@mi_app.get ("/lista")
def clientes ():
    nombres= ["daniela","zuleima","william","lupe","michael","sebastian","suns"]
    return {"clientes": nombres}