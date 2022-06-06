# Proyecto final - Mateo Algañaras, Maxi Romani, Maximiliano Rivera Miño

## Descargar:
    Desde una consola o el bash de git usar el siguiente comando
        git clone https://github.com/Tutealga/proyectofinal

## Instalacion:
    * pip install -r requirements.txt
    * python manage.py migrate
    * python manage.py runserver

## Funcionamiento:
   Al ingresar a la web nos encontramos con la pagina de inicio, donde cuenta con un navbar para ir a las diferentes secciones del sitio (productos, usuarios, comentarios, crear nuevo producto, crear nuevo usuario y crear nuevo comentario) y en el mismo un buscador para encontrar en la base de datos los diferentes modelos. Tambien en su contenido hay 3 cards para ir a las secciones del sitio, donde podemos ver o crear de los diferentes modelos.

   La pagina de inicio, como las demas paginas del sitio web, heredan el navbar (con sus secciones y buscador) del template 'base.html', el cual cuenta con un bloque para incrustar los diferentes contenidos de sus respectivas paginas (en el caso de productos que muestre productos, en el de usuarios usuarios y asi con todas).

   Para encontrar los diferentes modelos en el buscador hay que hacerlo segun el dato del modelo, en el caso de productos y usuarios por el nombre y en caso de los comentarios por su id.

   Las secciones de productos, usuarios y comentarios muestran mediante un bucle sus modelos respectivos, donde cada uno cuenta con una card distinta, con informacion dependiendo de su modelo. En el caso de los productos: nombre, precio, sku y stock (este se utiliza en un condicional para que si no tiene stock no se muestre). En el caso de los usuarios: nombre, edad, fecha de alta y DNI. En el caso de los comentarios: el comentario en si y una puntuacion.

   Por otro lado, las secciones de crear nuevo producto, usuario y comentario, cuentan cada uno con un formulario para crear estos mismos con sus diferentes datos que requiere el modelo.

   



   