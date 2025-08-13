def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t\t ... ⚠️ Oprima cualquier tecla para continuar ⚠️ ...")

def mostrar_menu_inicio():
    print("\n \t.:: Sistema de Gestión de Inventario ::.. \n\t\t1️⃣ .- 📝 Registro  \n\t\t2️⃣ .- 🔑 Login \n\t\t3️⃣ .- 🚪 Salir ")
    opcion = input("\t\t ➡️ Elige una opción: ").upper().strip()
    return opcion

def menu_usuario_logueado(id_usuario, nombre, email):
    print(f"\n\t 👋 Bienvenido {nombre} ({email})")
    print("\n \t.:: Sistema de Gestión de Productos y Más ::.. \n\t\t1️⃣ .- 🛒 Agregar Productos  \n\t\t2️⃣ .- 🚚 Agregar Proveedores \n\t\t3️⃣ .- 🏷️ Agregar Categoría \n\t\t4️⃣ .- 🚪 SALIR ")
    opcion = input("\t\t ➡️ Elige una opción: ").upper().strip()
    return opcion

def menu_productos():
    print("\n \t .::  Menú de Productos ::. \n\t1️⃣ .- ➕ Agregar Productos \n\t2️⃣ .- 📋 Mostrar Productos \n\t3️⃣ .- ✏️ Modificar Producto \n\t4️⃣ .- 🗑️ Borrar Productos \n\t5️⃣ .- 🚪 SALIR")
    opcion = input("\t\t ➡️ Elige una opción: ").upper().strip()
    return opcion

def menu_proveedores():
    print("\n \t .::  Menú de Proveedores ::. \n\t1️⃣ .- ➕ Agregar Proveedores \n\t2️⃣ .- 📋 Mostrar Proveedores \n\t3️⃣ .- ✏️ Modificar Proveedores \n\t4️⃣ .- 🗑️ Borrar Proveedores \n\t5️⃣ .- 🚪 SALIR")
    opcion = input("\t\t ➡️ Elige una opción: ").upper().strip()
    return opcion

def menu_categoria():
    print("\n \t .::  Menú de Categoría ::. \n\t1️⃣ .- ➕ Agregar Categoría \n\t2️⃣ .- 📋 Mostrar Categorías \n\t3️⃣ .- 🗑️ Borrar Categorías \n\t4️⃣ .- 🚪 SALIR")
    opcion = input("\t\t ➡️ Elige una opción: ").upper().strip()
    return opcion

