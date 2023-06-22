# chr_implementacion

Solucion a retos planteados en el test practico.

## Resumen

Para el reto se implemento un proyecto en django 4.0 el cual recibe el nombre app_chr este contiene los siguientes archivos
app_chr: carpeta con la configuracion incial de django
reto1: carpeta la cual cuenta con los archivos del codigo de la tarea 1
reto2: carpeta la cual cuenta con los archivos del codigo de la tarea 2
chromedriver_linux64: carpeta la cual contiene el driver de chrome selenium web dirver libreria la cual se usa en el reto2
.env: archivo el cual contiene las credenciales para la conexion con la base de datos postgresql
manage.py: archivo incial de django
output_datos_tabla.json: archivo resultante del reto2
requirements.txt: archivo el cual contiene los requerimientos del proyecto

### Reto 1

Se creo una nueva url llamada **get_jurisprudencia** a la cual se puede acceder de la forma http://localhost:8000/get_jurisprudencia/

Para este reto se realizo la peticion POST al url proporcionado y se proceso esta para obtener la informacion de las
jurisprudencias, esta contaba con un diccionario de datos anidados en al estructura de cada jurisprudencia los cuales 
recibian el nombre de "valores" para guardar cada registro se crearon dos modelos uno el cual guardaba la jurisprudencia
y un segundo el cual guardaba los valores los dos modelos estan realacionados, luego de ya tener la informacion procesada y alamacenada 
esta se conecta con la vista de administrador y se muestra al usuario

Cuando se hace la consulta mediante el navegador a la url **get_jurisprudencia** se lleva acabo el proceso previamente descrito para el reto 1

### Reto 2

Se creo una nueva url llamada **get_concesiones** a la cual se puede acceder de la forma http://localhost:8000/get_concesiones/

Para este reto se descargo el driver del navegador chrome para usarlo con selenium, con la libreria selenium se realizo una consulta a la url
que contenia la informacion de las conciliasiones maritimas en esta se ingresaron los filtros proporcionados por el reto y se realizo la busqueda
una vez mostrada la tabla de los resultados de esta de extrajo la infomacion objetivo iterando sobre esta y haciendo los cambios de las paginas
luego de tener todos los datos en una estructura de datos estos se convirtieron a un archvio .json el cual recibe el nombre de output_datos_tabla y
se encontra en este reporistorio posteriormente se insertaron eestos datos a la base usando el modelo creado para la informacion de las concesiones maritimas

Cuando se hace la consulta mediante el navegador a la url **get_concesiones** se lleva acabo el proceso previamente descrito para el reto 2


## Instalación

1. Clona el repositorio en tu máquina local:

```shell
git clone https://github.com/Ovidio-Git/chr_implementacion.git
```

2. Instalacion de dependencias

```shell
pip install -r requirements.txt
```


## Uso

1. Realiza las migraciones de la base de datos:

```shell
python manage.py migrate
```

2. Iniciar servidor de la aplicacion

```shell
python manage.py runserver
```

Abrir navegador web y visitar http://localhost:8000 para ver la aplicación en funcionamiento.


3. Ejecutar el proceso que da solucion al reto 1

Consultar la url ttp://localhost:8000/get_jurisprudencia/

4. Ejecutar el proceso que da solucion al reto 2

Consultar la url ttp://localhost:8000/get_concesiones/

