TRABAJO FINAL --  José Antonio Lera Romero

OBJETIVO DEL PROGRAMA

Se crea una base llamada: inventario.db
Se crea una tabla de Productos tiene los siguientes campos con sus siguientes formatos.
CREATE TABLE "productos" (
	"nombre"	TEXT NOT NULL,
	"descripcion"	TEXT,
	"categoria"	TEXT NOT NULL,
	"cantidad"	INTEGER NOT NULL,
	"precio"	NUMERIC NOT NULL,
	"id"	INTEGER,	PRIMARY KEY("id" AUTOINCREMENT) );

Se desarrollo un menu con las siguientes opciones todas fueron creadas como funciones:

“Crear menú” esta función debe mostrar el menú y permitir elegir una opción.

“Agregar Producto” esta función permitirá agregar un producto a la base inventario.db


“Mostrar Producto” esta función permitirá mostrar un producto a la base inventario.db

“Actualizar Cantidad de Producto” esta función permitirá actualizar todos los campos de un producto de la base inventario.db

“Eliminar Producto” esta función permitirá eliminar un producto de la base inventario.db

"Buscar Producto" esta función permite buscar un producto utilizando parte del nombre.

"Reporte de Bajo Stock" esta función solicita un valor de umbral del cual todo producto cuya cantidad sea menor será mostrado.


Estos fueron todos los pasos que se siguieron: 
1)	Crear una base en sqlite que se llame inventario.db 
2)	Crear una tabla que se llame “productos” que si no existe deberá crearse
3)	Crear las funciones enunciadas anteriormente
4)	Crear el main que llame únicamente a las funciones creadas.


