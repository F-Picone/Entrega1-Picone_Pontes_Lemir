# Entrega1-Picone_Pontes_Lemir
#PAGINA
En principio cuando entramos a la web, nos tenemos que dirigir a la aplicacion SaludApp/
Una ves dentro de la aplicacion, tendremos varias solapas en el head:
 - Inicio.
 - Medicos.
 - Especialidades.
 - Sedes.
El inicio sera un boton para volver a la pagina default.
Medicos es una solapa en donde vamos a poder buscar los medicos que trabajan en los distintos institutos de las sedes.
Especialidades es una solapa donde se indicara como bien se llama, las especialidades de estos centros medicos.
En la solapa sedes podremos ver donde estan ubicados los distintos institutos medicos.
Luego, por ultimo, tendremos un boto de Sacar turno, en donde si se apreta, te llevara a una pagina con un formulario para rellenar y hacer la solicitud para entrar como nuevo paciente en los institutos. 
#VISUAL ESTUDIO CODE
Vamos a tener dos principales carpetas. ProyectoFinalCH que es principalmente para los settings y redireccionar los links de las apps ahi. Para esta primera entrega no se trabajo ahi practicamente. 
La segunda carpeta principal es la de la propia app "SaludApp". En esta solapas nos encontraremos con la carpeta static, en donde estara cargada la plantilla utilizada para realizar la pagina web. Luego tendremos la carpeta templates/SaludApp en donde se estaran guardando todas las plantillas html usada para la pagina principal y las distintas solapas de la propia pagina. 
Como archivos extras tambien estan presente urls.py, el cual, posee las urls de las paginas de la propia app y las redirecciona a la carpeta de urls principal ubicada en ProyectoFinalCH. Otro archivo extra presente es el de forms.py, el cual se utilizo para realizar el formulario de la solicitud de turno. Despues otro archivos que se han utilizado fueron views.py, para generar todas las vistas de la app, models.py para generar todos los objetos que utiliza la app y admin.py para dar de alta el panel de administrador y acceder de manera mas directa a la base de datos.
