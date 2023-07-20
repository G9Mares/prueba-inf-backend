# Prueba tecnica Gustavo Mares 

## Descripcion

Este proyecto es el backend de un login y pagina de registro, parte de una prueba tecnica para full-stack jr

## Lenjuage y Framework de desarrollo

Se desarrollo usando python3 puntualmente usando el framework Fast API.

## Requisitios

Para su correcta ejecucion se recomienda tener instalado Xampp para acceder a una base de datos en local, de no ser asi se puede modificar la conexion la db en el archivo dbconexion, tambien se recomienda apliamnete ejcutarlo en un entorno virtual

## Instrucciones de uso

primero hay que clonar el repositorio en local desde la consola usando el comando

git clone https://github.com/G9Mares/prueba-inf-backend.git

posterior:

cd prueba-inf-backend

una vez en la ruta del proyecto crearemos y activaremos un entorno virtual y ejecutaremos el comando:

pip install -r requirements.txt

Cuando se terminen de descargar todas las dependencias ejecutaremos , este comando se encuentra tambien como comentario en main.py:

python -m uvicorn main:app --reload --port 4000 

## Caracteristicas y comentarios

Prefiero usar el framework de Fast API, debido a que es mas intuitivo, mas rapido y con mejores caracteristica, como una autodocumetacion, 
si nos dirigimos a la ruta que arroja cuando iniciamos el server /docs veremos una documentacion muy basica pero funcional de la api.

Se recomienda usar post man para pruebas
