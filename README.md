# Movies
Plataforma de Información de Peliculas

## Despliegue
Este repo incluye una DB SQLite con datos demo.
Se recomienda utilizar un virtualenv para desplegar esta aplicacion. \
Si se utiliza la base de datos de demo:

1. pip install -r requirements.txt
2. python manage.py runserver

En el caso de utilizar una DB nueva:
1. pip install -r requirements.txt
2. python manage.py makemigrations
3. python manage.py migrate
4. python manage.py runserver

## Subir imagenes
1. Para subir imagenes, necesitas un _superuser_, ejecuta el siguiente comando y sigue los pasos:
````sh
python manage.py createsuperuser
````
2. Accede al admin _http://[hostip]:8000/admin_
3. Crea un nuevo registro en el modelo _People Image_
4. El campo _People_ es un listado separado por comas, si se quiere añadir mas de un _People_ a una imagen, añada a la lista el nombre separado por coma


# Movies
Movies Information Platform

## Deployment
This repo includes a SQLite DB with demo data. 
Is recommended to use a virtualenv to deploy this application. \
If use the default SQLite DB, access to the folder and execute:

1. pip install -r requirements.txt
2. python manage.py runserver

In case of start new DB:
1. pip install -r requirements.txt
2. python manage.py makemigrations
3. python manage.py migrate
4. python manage.py runserver

## Upload images
1. To upload images, you need a _superuser_, execute and follow steps:
````sh
python manage.py createsuperuser
````
2. Access to admin _http://[hostip]>:8000/admin_
3. Create new register on _People Image_ model
4. The _People_ field is a Comma Separated list, if you want to assign the same image to more than one _People_, add it separated by comma
