# API de Clientes

# Información general
Este proyecto consiste en el desarrollo de una API básica utilizando el framework FastAPI en Python.  
La finalidad principal de la aplicación es mostrar información relacionada con un proyecto y retornar una lista de clientes mediante diferentes rutas o endpoints.

FastAPI es un framework moderno que permite crear APIs rápidas, organizadas y fáciles de mantener.

# Inicio

Para comenzar el desarrollo de la actividad, se creó una carpeta llamada `actividad framework kamila` en el escritorio.  
Posteriormente, la carpeta fue abierta desde Visual Studio Code para iniciar la programación y configuración del entorno de trabajo.

## Estructura del proyecto

Dentro de la carpeta principal se encuentran los siguientes archivos y carpetas:

`venv`
`main.py`
`README.md`

### Explicación

 `venv`: corresponde al entorno virtual donde se instalan las librerías necesarias para el proyecto.
 `main.py`: archivo principal donde se encuentra el código de la API.
`README.md`: documento utilizado para explicar el funcionamiento y desarrollo del proyecto.

---

# Creación del entorno virtual

Desde la terminal integrada de Visual Studio Code se ejecutó el siguiente comando:
py -m venv venv

# Explicación
Este comando permite crear un entorno virtual llamado `venv`.  
El entorno virtual sirve para instalar dependencias de manera independiente, evitando modificar la instalación principal de Python del equipo.



# Activación del entorno virtual

Después de crear el entorno virtual, se utilizó el siguiente comando para activarlo:

.\venv\Scripts\activate

## Explicación

Cuando el entorno virtual se activa correctamente, el nombre `(venv)` aparece al inicio de la terminal.  
Esto indica que todas las librerías que se instalen quedarán almacenadas únicamente dentro del proyecto.

# Instalación de FastAPI

Con el entorno virtual activo, se procedió a instalar FastAPI utilizando el siguiente comando:


pip install "fastapi[standard]"


# Explicación

Este comando instala el framework FastAPI junto con las herramientas necesarias para ejecutar correctamente la API.



# pip list 

Para comprobar que FastAPI fue instalado correctamente, se utilizó el siguiente comando:

pip list

## Explicación

El comando `pip list` permite visualizar todas las librerías instaladas dentro del entorno virtual.

---

# Creación del archivo principal

Posteriormente se creó el archivo `main.py`, el cual contiene la lógica principal de la API y la definición de las rutas.

## Código utilizado

```python
from fastapi import FastAPI

mi_app= FastAPI ()

@mi_app.get ("/mensaje")

def proyecto  ():
    return{"proyecto": "este es el proyecto de clientes a desarrollar"}


@mi_app.get ("/lista")
def clientes ():
    nombres= ["daniela","zuleima","william","lupe","michael","sebastian","suns"]
    return {"clientes": nombres}
```

---

# Explicación del código

# Importación de FastAPI

from fastapi import FastAPI

 Explicación

Esta línea permite importar la clase `FastAPI`, necesaria para construir la aplicación web.

# Creación de la aplicación principal

mi_app= FastAPI ()

### Explicación

Aquí se crea la aplicación principal llamada `mi_app`.  
Esta variable será utilizada para configurar y administrar todas las rutas de la API.

# Endpoint de mensaje

```python
@mi_app.get ("/mensaje")

def proyecto  ():
    return{"proyecto": "este es el proyecto de clientes a desarrollar"}
```

# Explicación
Este endpoint crea la ruta `/mensaje`.  
Cuando un usuario accede a esta dirección desde el navegador, la API devuelve una respuesta en formato JSON con información relacionada al proyecto.

# Resultado
{
    "proyecto": "este es el proyecto de clientes a desarrollar"
}

---

# Endpoint de lista de clientes

```python
@mi_app.get ("/lista")
def clientes ():
    nombres= ["daniela","zuleima","william","lupe","michael","sebastian","suns"]
    return {"clientes": nombres}
```

# Explicación

Este endpoint crea la ruta `/lista`.  
La función almacena varios nombres dentro de una lista y posteriormente retorna la información en formato JSON.

### Resultado esperado


{
    "clientes": [
        "daniela",
        "zuleima",
        "william",
        "lupe",
        "michael",
        "sebastian",
        "suns"
    ]
}


# Ejecución de la API

Para ejecutar la aplicación se utilizó el siguiente comando:


fastapi dev main.py

# Explicación

Este comando inicia el servidor local de FastAPI y permite acceder a la aplicación desde el navegador.



# Resultado

Después de ejecutar el proyecto, la API quedó disponible en la siguiente dirección local:

http://127.0.0.1:8000

# Rutas disponibles

Las rutas disponibles dentro de la API son:

 `/mensaje`
 `/lista`

---

# Conclusión

Gracias al uso de FastAPI fue posible desarrollar una API sencilla y funcional capaz de retornar información en formato JSON mediante diferentes endpoints.  
Además, el uso del entorno virtual permitió mantener organizadas las dependencias del proyecto y trabajar de forma más segura y estructurada.