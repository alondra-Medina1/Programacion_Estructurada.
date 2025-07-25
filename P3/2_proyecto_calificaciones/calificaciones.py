import mysql.connector
from mysql.connector import Error
import os

def borrarPantalla():
    os.system("cls")

def esperarTecla():
    input("\n⏳ Presiona cualquier tecla para continuar...")

def conectar():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_calificaciones"
        )
    except Error as e:
        print(f"⚠️ Error de conexión: {e}")
        return None

def agregarCalificaciones(_):
    borrarPantalla()
    conexion = conectar()
    if not conexion:
        return

    print("📝 Agregar Calificaciones")
    nombre = input("👤 Nombre del Alumno: ").upper().strip()
    califs = []

    for i in range(1, 4):
        while True:
            try:
                cal = float(input(f"📌 Calificación {i}: "))
                if 0 <= cal <= 10:
                    califs.append(cal)
                    break
                else:
                    print("❗ Ingresa un número válido (0-10)")
            except ValueError:
                print("❗ Ingresa un valor numérico")

    cursor = conexion.cursor()
    sql = "INSERT INTO alumno (nombre, calificacion1, calificacion2, calificacion3) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (nombre, *califs))
    conexion.commit()
    print("✅ Calificaciones registradas con éxito")
    cursor.close()

def mostrarCalificaciones(_):
    borrarPantalla()
    conexion = conectar()
    if not conexion:
        return

    print("📄 Mostrar Calificaciones")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM alumno")
    registros = cursor.fetchall()

    if registros:
        print("\n📋 Alumnos Registrados")
        print(f"{'🆔 ID':<5} {'👤 Nombre':<12} {'📘 C1':<10} {'📗 C2':<10} {'📙 C3':<10}")
        print("-" * 50)
        for id, nombre, c1, c2, c3 in registros:
            print(f"{id:<5} {nombre:<12} {c1:<10} {c2:<10} {c3:<10}")
        print("-" * 50)
    else:
        print("❌ No hay calificaciones registradas")
    cursor.close()

def calcularPromedios(_):
    borrarPantalla()
    conexion = conectar()
    if not conexion:
        return

    print("📊 Calcular Promedios")
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, calificacion1, calificacion2, calificacion3 FROM alumno")
    registros = cursor.fetchall()

    if registros:
        print("\n📈 Promedios por Alumno")
        print(f"{'👤 Alumno':<15} {'📏 Promedio':<10}")
        print("-" * 30)
        total = 0

        for nombre, c1, c2, c3 in registros:
            promedio = (c1 + c2 + c3) / 3
            print(f"{nombre:<15} {promedio:<10.2f}")
            total += promedio

        promedio_general = total / len(registros)
        print("-" * 30)
        print(f"📌 Promedio grupal: {promedio_general:.2f}")
    else:
        print("❌ No hay calificaciones registradas")
    cursor.close()

def buscarAlumno(_):
    borrarPantalla()
    conexion = conectar()
    if not conexion:
        return

    print("🔍 Buscar Alumno")
    nombre = input("🧾 Nombre del alumno: ").upper().strip()

    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM alumno WHERE nombre = %s", (nombre,))
    registros = cursor.fetchall()

    if registros:
        print("\n📋 Resultado de Búsqueda")
        print(f"{'🆔 ID':<5} {'👤 Nombre':<12} {'📘 C1':<10} {'📗 C2':<10} {'📙 C3':<10}")
        print("-" * 50)
        for id, nombre, c1, c2, c3 in registros:
            print(f"{id:<5} {nombre:<12} {c1:<10} {c2:<10} {c3:<10}")
        print("-" * 50)
    else:
        print("❌ Alumno no encontrado")
    cursor.close()
