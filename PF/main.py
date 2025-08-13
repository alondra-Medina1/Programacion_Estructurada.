import funciones
import conexionBD
from usuarios import usuario
from categorias import categoria
from productos import producto
from proveedores import proveedor
import getpass


def main():
    opcion = True
    while opcion:
        funciones.borrarPantalla()
        opcion = funciones.mostrar_menu_inicio().strip().upper()

        # 📝 REGISTRO DE USUARIO
        if opcion == "1" or opcion == "REGISTRO":
            funciones.borrarPantalla()
            print("\n\t📝 ..:: Registro en el Sistema ::..")
            
            nombre = input("\t👤 ¿Cuál es tu nombre?: ").upper().strip()
            apellidos = input("\t👥 ¿Cuáles son tus apellidos?: ").upper().strip()
            email = input("\t📧 Ingresa tu email: ").lower().strip()
            password = getpass.getpass("\t🔑 Ingresa tu contraseña: ").strip()
            confirmar = getpass.getpass("\t🔒 Confirma tu contraseña: ").strip()

            if not nombre or not apellidos or not email or not password:
                print("\n\t⚠️ Todos los campos son obligatorios.")
            elif password != confirmar:
                print("\n\t❌ Las contraseñas no coinciden.")
            else:
                lista_usuario = usuario.registrar(nombre, apellidos, email, password)
                if lista_usuario:
                    print(f"\n\t✅ {nombre} {apellidos} registrado correctamente con el email {email}")
                else:
                    print("\n\t🚫 No es posible registrar el usuario, inténtalo más tarde.")
            funciones.esperarTecla()

        # 🔓 LOGIN
        elif opcion == "2" or opcion == "LOGIN":
            funciones.borrarPantalla()
            print("\n\t🔓 ..:: Inicio de Sesión ::..")
            
            email = input("\t📧 Ingresa tu E-mail: ").lower().strip()
            password = getpass.getpass("\t🔑 Ingresa tu contraseña: ").strip()
            lista_usuario = usuario.inicio_sesion(email, password)

            if lista_usuario:
                menu_usuario_logueado_principal(lista_usuario[0], lista_usuario[1], lista_usuario[2])
            else:
                print("\n\t❌ E-mail y/o contraseña incorrectos. Verifica y vuelve a intentar.")
                funciones.esperarTecla()

        # 🚪 SALIR
        elif opcion == "3" or opcion == "SALIR":
            print("\n\t👋 Terminó la ejecución del sistema. ¡Hasta pronto!")
            opcion = False
            funciones.esperarTecla()

        # ❌ OPCIÓN INVÁLIDA
        else:
            print("\n\t⚠️ Opción no válida")
            funciones.esperarTecla()


def menu_usuario_logueado_principal(usuario_id, nombre_usuario, apellidos):
    productos = []
    proveedores = []
    categorias = []

    while True:
        funciones.borrarPantalla()
        print(f"\n\t👋 Bienvenido {nombre_usuario} {apellidos}")
        opcion = funciones.menu_usuario_logueado(usuario_id, nombre_usuario, apellidos)

        # 🛒 MENÚ PRODUCTOS
        if opcion == "1":
            while True:
                funciones.borrarPantalla()
                opcion_producto = funciones.menu_productos()

                if opcion_producto == "1":
                    nombre_producto = input("\n\t🏷️ Nombre del producto: ").strip()
                    try:
                        precio = float(input("\t💲 Precio: ").strip())
                        cantidad = int(input("\t📦 Cantidad: ").strip())
                        producto_nuevo = {"nombre": nombre_producto, "precio": precio, "cantidad": cantidad}
                        productos.append(producto_nuevo)
                        print("\t✅ Producto agregado con éxito.")
                    except ValueError:
                        print("\t❌ Precio o cantidad inválidos.")
                    funciones.esperarTecla()

                elif opcion_producto == "2":
                    if not productos:
                        print("\n\t📭 No hay productos registrados.")
                    else:
                        print("\n\t📋 Lista de productos:")
                        for i, p in enumerate(productos, 1):
                            print(f"\t{i}. 🏷️ {p['nombre']} | 💲 {p['precio']} | 📦 {p['cantidad']}")
                    funciones.esperarTecla()

                elif opcion_producto == "3":
                    if not productos:
                        print("\n\t📭 No hay productos para modificar.")
                    else:
                        for i, p in enumerate(productos, 1):
                            print(f"\t{i}. 🏷️ {p['nombre']} | 💲 {p['precio']} | 📦 {p['cantidad']}")
                        try:
                            indice = int(input("\n\t✏️ Número del producto a modificar: ")) - 1
                            if 0 <= indice < len(productos):
                                productos[indice]["nombre"] = input("\t🏷️ Nuevo nombre: ").strip()
                                productos[indice]["precio"] = float(input("\t💲 Nuevo precio: ").strip())
                                productos[indice]["cantidad"] = int(input("\t📦 Nueva cantidad: ").strip())
                                print("\t✅ Producto modificado.")
                            else:
                                print("\t❌ Número inválido.")
                        except ValueError:
                            print("\t❌ Entrada no válida.")
                    funciones.esperarTecla()

                elif opcion_producto == "4":
                    if not productos:
                        print("\n\t📭 No hay productos para borrar.")
                    else:
                        for i, p in enumerate(productos, 1):
                            print(f"\t{i}. 🏷️ {p['nombre']} | 💲 {p['precio']} | 📦 {p['cantidad']}")
                        try:
                            indice = int(input("\n\t🗑️ Número del producto a borrar: ")) - 1
                            if 0 <= indice < len(productos):
                                eliminado = productos.pop(indice)
                                print(f"\t🗑️ Producto '{eliminado['nombre']}' eliminado.")
                            else:
                                print("\t❌ Número inválido.")
                        except ValueError:
                            print("\t❌ Entrada no válida.")
                    funciones.esperarTecla()

                elif opcion_producto == "5":
                    break

                else:
                    print("\n\t⚠️ Opción inválida.")
                    funciones.esperarTecla()

        # 🚚 MENÚ PROVEEDORES
        elif opcion == "2":
            while True:
                funciones.borrarPantalla()
                opcion_prov = funciones.menu_proveedores()

                if opcion_prov == "1":
                    nombre = input("\n\t🏢 Nombre del proveedor: ").strip()
                    telefono = input("\t📞 Teléfono: ").strip()
                    email = input("\t📧 Correo electrónico: ").strip()
                    prov = {"nombre": nombre, "telefono": telefono, "email": email}
                    proveedores.append(prov)
                    print("\t✅ Proveedor agregado correctamente.")
                    funciones.esperarTecla()

                elif opcion_prov == "2":
                    if not proveedores:
                        print("\n\t📭 No hay proveedores registrados.")
                    else:
                        print("\n\t📋 Lista de proveedores:")
                        for i, p in enumerate(proveedores, start=1):
                            print(f"\t{i}. 🏢 {p['nombre']} | 📞 {p['telefono']} | 📧 {p['email']}")
                    funciones.esperarTecla()

                elif opcion_prov == "3":
                    if not proveedores:
                        print("\n\t📭 No hay proveedores para modificar.")
                    else:
                        for i, p in enumerate(proveedores, 1):
                            print(f"\t{i}. 🏢 {p['nombre']} | 📞 {p['telefono']} | 📧 {p['email']}")
                        try:
                            idx = int(input("\n\t✏️ Número del proveedor a modificar: ")) - 1
                            if 0 <= idx < len(proveedores):
                                proveedores[idx]["nombre"] = input("\t🏢 Nuevo nombre: ").strip()
                                proveedores[idx]["telefono"] = input("\t📞 Nuevo teléfono: ").strip()
                                proveedores[idx]["email"] = input("\t📧 Nuevo correo: ").strip()
                                print("\t✅ Proveedor modificado.")
                            else:
                                print("\t❌ Número inválido.")
                        except:
                            print("\t❌ Entrada inválida.")
                    funciones.esperarTecla()

                elif opcion_prov == "4":
                    if not proveedores:
                        print("\n\t📭 No hay proveedores para borrar.")
                    else:
                        for i, p in enumerate(proveedores, 1):
                            print(f"\t{i}. 🏢 {p['nombre']} | 📞 {p['telefono']} | 📧 {p['email']}")
                        try:
                            idx = int(input("\n\t🗑️ Número del proveedor a eliminar: ")) - 1
                            if 0 <= idx < len(proveedores):
                                eliminado = proveedores.pop(idx)
                                print(f"\t🗑️ Proveedor '{eliminado['nombre']}' eliminado.")
                            else:
                                print("\t❌ Número inválido.")
                        except:
                            print("\t❌ Entrada no válida.")
                    funciones.esperarTecla()

                elif opcion_prov == "5":
                    break

                else:
                    print("\n\t⚠️ Opción no válida.")
                    funciones.esperarTecla()

        # 📂 MENÚ CATEGORÍAS
        elif opcion == "3":
            while True:
                funciones.borrarPantalla()
                opcion_cat = funciones.menu_categoria()

                if opcion_cat == "1":
                    nombre = input("\n\t🏷️ Nombre de la categoría: ").strip()
                    categorias.append(nombre)
                    print(f"\t✅ Categoría '{nombre}' agregada con éxito.")
                    funciones.esperarTecla()

                elif opcion_cat == "2":
                    if not categorias:
                        print("\n\t📭 No hay categorías registradas.")
                    else:
                        print("\n\t📋 Lista de categorías:")
                        for i, cat in enumerate(categorias, start=1):
                            print(f"\t{i}. 🏷️ {cat}")
                    funciones.esperarTecla()

                elif opcion_cat == "3":
                    if not categorias:
                        print("\n\t📭 No hay categorías para borrar.")
                    else:
                        print("\n\t📋 Categorías disponibles:")
                        for i, cat in enumerate(categorias, start=1):
                            print(f"\t{i}. 🏷️ {cat}")
                        try:
                            idx = int(input("\n\t🗑️ Número de la categoría a eliminar: ")) - 1
                            if 0 <= idx < len(categorias):
                                eliminado = categorias.pop(idx)
                                print(f"\t🗑️ Categoría '{eliminado}' eliminada.")
                            else:
                                print("\t❌ Número inválido.")
                        except:
                            print("\t❌ Entrada no válida.")
                    funciones.esperarTecla()

                elif opcion_cat == "4":
                    break

                else:
                    print("\n\t⚠️ Opción inválida.")
                    funciones.esperarTecla()

        # 🚪 SALIR DEL MENÚ PRINCIPAL
        elif opcion == "4":
            print("\n\t👋 Gracias por usar el sistema. ¡Hasta luego!")
            break

        else:
            print("\n\t⚠️ Opción inválida.")
            funciones.esperarTecla()


if __name__ == "__main__":
    main()
