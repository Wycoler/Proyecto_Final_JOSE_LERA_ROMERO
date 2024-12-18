import sqlite3

def crear_tabla():
    "Crea la tabla 'productos' en la base de datos si no existe la crea."
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        descripcion TEXT,
                        categoria TEXT NOT NULL,
                        cantidad INTEGER NOT NULL,
                        precio REAL NOT NULL)''')
    conexion.commit()
    conexion.close()

def agregar_producto():
    "Permite agregar un producto a la tabla de productos de la base inventario.db"
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripcion del producto: ")
    categoria = input("Ingrese la categoria del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO productos (nombre, descripcion, categoria, cantidad, precio) VALUES (?, ?, ?, ?, ?)", (nombre, descripcion, categoria, cantidad, precio))
    conexion.commit()
    conexion.close()
    print("Producto agregado correctamente.")

def mostrar_productos():
    "Muestra todos los productos"
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conexion.close()

    if productos:
        print("\nProductos en inventario:")
        print("ID | Nombre | Descripción | Categoría | Cantidad | Precio")
        print("-" * 60)
        for producto in productos:
            print(f"{producto[0]} | {producto[1]} | {producto[2]} | {producto[3]} | {producto[4]} | {producto[5]:.2f}")
    else:
        print("No hay productos en el inventario")

def actualizar_producto():
    "Actualiza todos los campos de un producto"
    id_producto = int(input("Ingrese el ID del producto a actualizar: "))
    nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
    nueva_descripcion = input("Ingrese la nueva descripción del producto: ")
    nueva_categoria = input("Ingrese la nueva categoría del producto: ")
    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
    nuevo_precio = float(input("Ingrese el nuevo precio: "))

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE productos
        SET nombre = ?, descripcion = ?, categoria = ?, cantidad = ?, precio = ?
        WHERE id = ?
    """, (nuevo_nombre, nueva_descripcion, nueva_categoria, nueva_cantidad, nuevo_precio, id_producto))
    conexion.commit()
    conexion.close()
    print("Producto actualizado con éxito.")

def eliminar_producto():
    "Elimina un producto de la tabla productos"
    id_producto = int(input("Ingrese el ID del producto a eliminar: "))

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
    conexion.commit()
    conexion.close()
    print("Producto eliminado correctamente")

def buscar_producto():
    "Busca un producto por nombre o categoría."
    termino = input("Ingrese el nombre o la categoría del producto a buscar: ")

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE nombre LIKE ? OR categoria LIKE ?", (f"%{termino}%", f"%{termino}%"))
    productos = cursor.fetchall()
    conexion.close()

    if productos:
        print("\nResultados de la búsqueda:")
        print("ID | Nombre | Descripción | Categoría | Cantidad | Precio")
        print("-" * 60)
        for producto in productos:
            print(f"{producto[0]} | {producto[1]} | {producto[2]} | {producto[3]} | {producto[4]} | {producto[5]:.2f}")
    else:
        print("No se encontraron productos con ese criterio.")

def reporte_bajo_stock():
    "Muestra los productos con cantidad menor a un umbral"
    umbral = int(input("Ingrese el umbral de bajo stock: "))

    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE cantidad < ?", (umbral,))
    productos = cursor.fetchall()
    conexion.close()

    if productos:
        print("\nProductos con bajo stock:")
        print("ID | Nombre | Descripción | Categoría | Cantidad | Precio")
        print("-" * 60)
        for producto in productos:
            print(f"{producto[0]} | {producto[1]} | {producto[2]} | {producto[3]} | {producto[4]} | {producto[5]:.2f}")
    else:
        print("No hay productos con bajo stock.")

def mostrar_menu():
    "Muestra el menú y permite seleccionar una opción"
    while True:
        print("\nMenú del Sistema:")
        print("1. Agregar Producto")
        print("2. Mostrar Productos")
        print("3. Actualizar Producto")
        print("4. Eliminar Producto")
        print("5. Buscar Producto")
        print("6. Reporte de Bajo Stock")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            buscar_producto()
        elif opcion == "6":
            reporte_bajo_stock()
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def main():
    "Función principal del programa"
    crear_tabla()
    mostrar_menu()

if __name__ == "__main__":
    main()
