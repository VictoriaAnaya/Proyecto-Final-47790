# Proyecto Final Python 47790 - Gómez Anaya Victoria 
Entrega del proyecto final del curso de CoderHouse, comisión 47790, realizada por la alumna Gómez Anaya Victoria.

________________________________________

NOMBRE DEL PROYECTO

Quick Finance: blog de noticias.

________________________________________

VERSION

1.0

________________________________________

PROYECTO.

Este proyecto es desarrollado en Python utilizando el framework Django. El mismo trata de una app web sobre un foro de noticias, la cual renderiza la información que esta almacenada en la base de datos y la muestra en las diferentes vistas dependiendo cual sea la solicitud. 

A fin de navegar por las secciones de la página web, el usuario será requerido iniciar sesión o registrarse en caso de no contar con usuario o contraseña. En ambas opciones, una vez la página valide la autenticación del usuario, este será redirigido al inicio de la página web.

Los usuarios pueden realizar las siguientes accciones:
   - Publicar noticias.
   - Editar noticias anteriormente publicadas.
   - Comentar por medio del foto las noticias publicadas.
   - Editar el perfil de Usuario
   - Cambiar la contraseña de Usuario
   - Cerrar Sesión
   - Login en caso de haber cerrado sesión

Nota: La opción de editar y eliminar noticias solo le está permitido al autor de la publicación.
________________________________________

DOCUMENTACIÓN.

Para poder encontrar los archivos que nombrare a posterior ingresar en la carpeta AppCoder. Los archivos son: models.py, forms.py, urls.py, views.py, la carpeta de templates, entre otros.

________________________________________

TECNOLOGÍA UTILIZADA.

Front-End
•	HTML 5
•	CSS 3
•	Javascript ES6
•	Bootstrap 5.2

Back-End
•	Python 3.12.4
•	Django 5.0

________________________________________

MODELS.PY

En este archivo podemos encontrar los modelos de datos usados por el backend.

Usuario:

El modelo Usuario representa a los usuarios registrados en la aplicación. Contiene información sobre personas que utilizan la plataforma, incluyendo detalles como nombre, apellido, fecha de nacimiento, intereses y país de origen. Los campos típicos de este modelo incluyen:
	
    nombre (CharField): Almacena el nombre del usuario.
	apellido (CharField): Guarda el apellido del usuario.
	nacimiento (DateField o DateTimeField): Registra la fecha de nacimiento del usuario.
	intereses (TextField o algún otro tipo de campo de texto): Almacena los intereses del usuario, como una descripción más extensa.
	pais_origen (ForeignKey a un modelo Pais): Relaciona al usuario con su país de origen.

Pais:

El modelo Pais representa países que pueden asociarse con los usuarios. Este modelo posee los siguientes campos:
	
    nombre (CharField): Almacena el nombre del país.

Noticia:

El modelo Noticia representa las noticias publicadas en la plataforma. Contiene información sobre los artículos o noticias, incluyendo título, contenido y fecha de publicación. Los campos típicos de este modelo son:
	
    titulo (CharField): Almacena el título de la noticia.
	contenido (TextField o algún otro tipo de campo de texto): Guarda el contenido de la noticia.
	fecha_publicacion (DateField o DateTimeField): Registra la fecha en que se publicó la noticia.

Comentario:

El modelo Comentario permite asociar comentarios a usuarios y noticias, almacenar el contenido del comentario y registrar la fecha y hora de creación del comentario. 

    usuario (ForeignKey a Usuario): Este campo establece una relación muchos a uno con el modelo Usuario. Cada comentario está asociado a un usuario específico. Si un usuario se elimina, todos los comentarios asociados a ese usuario se eliminan.

    noticia (ForeignKey a Noticia): Similar al campo usuario, este campo establece una relación muchos a uno con el modelo Noticia. Cada comentario está asociado a una noticia específica. Si una noticia se elimina, todos los comentarios asociados a esa noticia se eliminan.

    contenido (TextField): Este campo almacena el contenido del comentario como texto. Puede contener una descripción detallada o cualquier otro tipo de información que el usuario haya ingresado.

    fecha_comentario (DateTimeField con auto_now_add=True): Este campo almacena la fecha y hora en que se creó el comentario. 

________________________________________

FORMS.PY

En este archivo se encuentran los formularios usados para cargar los datos que quedan guardados en la base de datos. Son 4 los formularios: 1- registrar usuarios, 2- buscar usuarios, 3- crear noticias, 4- buscar noticias. 
________________________________________

URLS.PY

Contiene cada una de las rutas de las vistas de la app.
________________________________________

VIEWS.PY

Aparecen todas las vistas que se utilizan en la app. Asociado a lo anterior por cada modelo se aplica el concepto de CRUD(Create, Read, Update, Delete); una vista de logueo, registro y edicion de perfil del usuario. 
________________________________________

TEMPLATES.

Es una carpeta donde se encuentran todos los archivos HTML, usados por la app. Se utiliza una platilla de BOOSTRAP y se aplica el concepto de herencia a cada archivo.
________________________________________

VIDEO DEMOSTRACIÓN.



________________________________________

Autora: Victoria Gomez Anaya
