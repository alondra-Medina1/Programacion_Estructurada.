import os
import mysql.connector
from mysql.connector import Error

def borrarPantalla():
    os.system("cls")

def esperarTecla():
    input("\n\t👉 Presiona ENTER para continuar...")

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_agenda"
        )
        return conexion
    except Error as e:
        print(f"❌ Error: {e}")
        return None

def agregarContacto(agenda):
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD:
        print("\n📇 .:: Agregar Contacto ::.")
        nombre = input("👤 Nombre: ").upper().strip()
        if nombre in agenda:
            print("\n❌ ¡Contacto ya existe! ❌")
        else:
            telefono = input("📞 Teléfono: ").strip()
            email = input("📧 Email: ").lower().strip()
            agenda[nombre] = [telefono, email]

            cursor = conexionBD.cursor()
            sql = "INSERT INTO contacto (nombre, telefono, email) VALUES (%s, %s, %s)"
            val = (nombre, telefono, email)
            cursor.execute(sql, val)
            conexionBD.commit()
            cursor.close()

            print("\n✅ Contacto agregado con éxito.")

def mostrarContactos(agenda):
    conexionBD = conectar()
    if conexionBD:
        borrarPantalla()
        print("\n📋 .:: Contactos Registrados ::.")
        cursor = conexionBD.cursor()
        cursor.execute("SELECT * FROM contacto")
        contactos = cursor.fetchall()

        if contactos:
            print(f"\n{'ID':<5} {'Nombre':<15} {'Teléfono':<15} {'Email':<25}")
            print("-" * 60)
            for id_, nombre, tel, email in contactos:
                print(f"{id_:<5} {nombre:<15} {tel:<15} {email:<25}")
            print("-" * 60)
        else:
            print("❌ No hay contactos en la agenda.")
        cursor.close()

def buscarContacto(agenda):
    conexionBD = conectar()
    if conexionBD:
        borrarPantalla()
        print("\n🔎 .:: Buscar Contacto ::.")
        nombre = input("🔍 Ingresa el nombre a buscar: ").upper().strip()

        cursor = conexionBD.cursor()
        sql = "SELECT * FROM contacto WHERE nombre = %s"
        cursor.execute(sql, (nombre,))
        contactos = cursor.fetchall()

        if contactos:
            print(f"\n{'ID':<5} {'Nombre':<15} {'Teléfono':<15} {'Email':<25}")
            print("-" * 60)
            for id_, nombre, tel, email in contactos:
                print(f"{id_:<5} {nombre:<15} {tel:<15} {email:<25}")
            print("-" * 60)
        else:
            print("\n❌ Contacto no encontrado.")
        cursor.close()

def modificarContacto(agenda):
    conexionBD = conectar()
    if conexionBD:
        borrarPantalla()
        print("\n✏️ .:: Modificar Contacto ::.")
        busqueda = input("🔍 Nombre del contacto a modificar: ").upper().strip()

        cursor = conexionBD.cursor()
        sql = "SELECT * FROM contacto WHERE nombre = %s"
        cursor.execute(sql, (busqueda,))
        contactos = cursor.fetchall()

        if contactos:
            print(f"\n{'ID':<5} {'Nombre':<15} {'Teléfono':<15} {'Email':<25}")
            print("-" * 60)
            for id_, nombre, tel, email in contactos:
                print(f"{id_:<5} {nombre:<15} {tel:<15} {email:<25}")
            print("-" * 60)

            id_sel = input("🆔 Selecciona el ID a modificar: ").strip()
            id_list = [str(c[0]) for c in contactos]

            if id_sel in id_list:
                resp = input(f"⚠️ ¿Modificar contacto '{busqueda}' con ID {id_sel}? (Si/No): ").upper().strip()
                if resp == "SI":
                    nombre = input("👤 Nuevo nombre: ").upper().strip()
                    telefono = input("📞 Nuevo teléfono: ").strip()
                    email = input("📧 Nuevo email: ").lower().strip()

                    sql = "UPDATE contacto SET nombre = %s, telefono = %s, email = %s WHERE id = %s"
                    cursor.execute(sql, (nombre, telefono, email, id_sel))
                    conexionBD.commit()
                    print("\n✅ Contacto modificado con éxito.")
            else:
                print("\n⚠️ ID inválido, inténtalo de nuevo.")
        else:
            print("❌ Contacto no encontrado.")
        cursor.close()

def eliminarContacto(agenda):
    conexionBD = conectar()
    if conexionBD:
        borrarPantalla()
        print("\n🗑️ .:: Eliminar Contacto ::.")
        nombre = input("🔍 Nombre del contacto a eliminar: ").upper().strip()

        cursor = conexionBD.cursor()
        sql = "SELECT * FROM contacto WHERE nombre = %s"
        cursor.execute(sql, (nombre,))
        contactos = cursor.fetchall()

        if contactos:
            print(f"\n{'ID':<5} {'Nombre':<15} {'Teléfono':<15} {'Email':<25}")
            print("-" * 60)
            for id_, nombre, tel, email in contactos:
                print(f"{id_:<5} {nombre:<15} {tel:<15} {email:<25}")
            print("-" * 60)

            id_sel = input("🆔 Selecciona el ID a eliminar: ").strip()
            id_list = [str(c[0]) for c in contactos]

            if id_sel in id_list:
                resp = input(f"⚠️ ¿Eliminar contacto '{nombre}' con ID {id_sel}? (Si/No): ").upper().strip()
                if resp == "SI":
                    sql = "DELETE FROM contacto WHERE id = %s"
                    cursor.execute(sql, (id_sel,))
                    conexionBD.commit()
                    print("\n✅ Contacto eliminado con éxito.")
            else:
                print("\n⚠️ ID inválido, inténtalo de nuevo.")
        else:
            print("❌ Contacto no encontrado.")
        cursor.close()
