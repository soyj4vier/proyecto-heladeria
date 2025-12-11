Credenciales Administrador y login de Django:
user: Administrador
contraseña: Ventana#123

RUTAS PARA CONSEGUIR TOKEN

ippublica/api/token
ippublica/api/token/refresh

Privilegios
Usuario administrador, puede hacer de todo GET, POST, PUT, DELETE
username:Administrador
password:Ventana#123

Usuario Vendedor, solo puede leer
username: nuevo_vendedor
password: Ventana#123

RUTAS de API

clientesapi/
clienteslistapi/
clienteslist/INSERTE ID

RUTAS API PROMOCIONES

promocionesapi/
promocioneslistapi/
promocioneslist/INSERTE ID

Descripcion breve del proyecto:

Funcion organizacional: marketing
Empresa: Secreto Helado
Descripción: Solución informatica para una pyme que pueda comenzar a valorar sus datos, con funcionalidades basicas de registros como CRUD en
nuestro caso como marketing un registro de clientes, promociones, etc.

Instruciones:

Instalación: Pasar el proyecto por a aplicacion Filezilla o por Putty a traves de la ip publica de la instancia aws.
Migración: Definir models.py, crear la base de datos y usuarios en la db, luego ejecutar los comandos makemigrations y migrate.
Ejecución: Entrar a la carpeta del proyecto, entrar en el entorno virtual y ejecutar "python3 manage.py runserver 0.0.0.0:8080", y por ultimo entrar a la pagina por el navegador con la ip publica de la instancia y el puerto (8080)
