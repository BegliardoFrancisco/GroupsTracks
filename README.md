

#  PARCIAL

Se debe utilizar la bdd 'chinook' para este proyecto.

Este es un ejemplo de API en python utilizando DDD, proveniente de un parcial de asignatura electiva backend de aplicaciones UTN CBA.

Esta a su vez se realizada utilizando Java con Sprint, Sprint boot en este caso fue adaptado para su implementacion en el lenguaje python.




## Enunciado:
### Objetivo:
Poner en práctica lo aprendido acerca de la  programación en el lado del backend utilizando:

- El lenguaje python y sus diferentes librerias.
- Administración del proyecto y dependencias del mismo utilizando entornos virtuales
-  El framework FastAPI, SQLAlchemy , asyncio (corrutinas y async/await)
- Conceptos de desarrollo y testing.

## Introducción:
Se brinda al estudiante la base de datos Chinook, la base de datos Chinook es una base de datos de 
ejemplo utilizada para probar funcionalidades de los motores de base de datos y que en este caso la 
vamos a utilizar como repositorio de datos del ejercicio del parcial.
Esta base de datos contiene los datos de una biblioteca de medios digitales que pueden ser accedidos 
para compra y reproducción, incluye tablas para artistas, álbumes, tracks, facturas, clientes y listas de 
reproducción.
A continuación, un breve detalle acerca de las tablas que incluye la base de datos:

- Employees (Empleados): Almacena datos de los empleados, como su ID de empleado, apellidos,  nombres, etc. También incluye un campo llamado "ReportsTo" para especificar quién reporta a quién.
- Customers (Clientes): Almacena datos de los clientes.
- Invoices (Facturas): Contiene datos de encabezado de facturas.
- Invoice_Items (Ítems_de_Factura): Almacena datos de los ítems de línea de las facturas.
- Artists (Artistas): Almacena información sobre los artistas, incluyendo sus IDs y nombres.
- Albums (Álbumes): Contiene datos relacionados con los álbumes.
- Media_Types (Tipos_de_Medios): Almacena tipos de medios, como archivos de audio MPEG y AAC.
- Genres (Géneros): Almacena tipos de música, como rock, jazz, metal, etc.
- Tracks (Pistas): Contiene datos de las canciones (pistas).
- Playlists (Listas_de_Reproducción): Almacena información sobre las listas de reproducción.
- Playlist_Track(Pista_de_Lista_de_Reproducción): Refleja la relación entre las listas de reproducción y las pistas. Se utiliza para representar esta relación de muchos a muchos.

## Se pide:
- Construir un proyecto  para conectarse a la base de datos, Endpoints para dar respuesta a los requisitos aquí solicitados, Tests unitarios de estos requisitos y la estructura interna vista en clase y acordada para la implementación.
- Construir la estructura de endpoints CRUD (Crear, Obtener, Modificar y Borrar) para cada una de las siguientes tablas:
    -  customer
    - invoice
    - invoice_items
    - playlist
    - playlist_track
    - track
    - genre
    - album
    - artist
-  Para cada una de estas tablas se solicita al menos, capa de acceso a datos (Repositorio), capa de negocio (Servicio) y capa de Interfaz (Controlador), además evidentemente de la Entidad de datos.



## Deployment

To deploy this project run

Clonar el repositorio

```bash
    git clone https://github.com/BegliardoFrancisco/GroupsTracks.git
```

Crear el entorno virtual

```bash
    python -m venv env
```

Activar entorno virtual
- En Windows:
```bash
    env\Scripts\activate
```
- En Linux y Mac OS:
```bash
    source env/bin/activate
```

Instalar dependencias: 

```bash 
    pip install -r requiriments.txt    
```

Ejecutar codigo:
 
```bash
    uvicorn main:app --reload 
```



## Authors
Este enunciado es proveniente de un examen de la asignatura electiva Backend de aplicaciones facultad regional de Cordoba UTN.

### Resolución por
- [Francisco Begliardo] (https://github.com/BegliardoFrancisco)

