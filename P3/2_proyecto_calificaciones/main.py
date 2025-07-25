'''
Proyecto 3
Crear un proyecto que permita Gestionar (Administrar) calificaciones; colocar un menu de opciones para agregar, mostrar y calcular
promedios de las calificaciones de los alumnos

Notas:
1.- Utilizar funciones y mandar llamar desde otro archivo
2.- Utilizar listas para almacenar el nombre de un alumno y 3 calificaciones
'''

import calificaciones

def main():
    opcion = True
    datos = []
    while opcion:
        calificaciones.borrarPantalla()
        print("\t\t📘 SISTEMA DE GESTIÓN DE CALIFICACIONES 📘")
        print("\t1️⃣.- Agregar")
        print("\t2️⃣.- Mostrar")
        print("\t3️⃣.- Calcular promedio")
        print("\t4️⃣.- Buscar Alumno")
        print("\t5️⃣.- Salir")
        opcion = input("\nOpción seleccionada: ").strip()

        match opcion:
            case "1":
                calificaciones.agregarCalificaciones(datos)
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrarCalificaciones(datos)
                calificaciones.esperarTecla()
            case "3":
                calificaciones.calcularPromedios(datos)
                calificaciones.esperarTecla()
            case "4":
                calificaciones.buscarAlumno(datos)
                calificaciones.esperarTecla()
            case "5":
                calificaciones.borrarPantalla()
                print("🚪 .::Terminaste de usar el programa::. 🚪")
                opcion = False
            case _:
                print("⚠️ Opción no válida, vuelve a intentarlo ⚠️")
                calificaciones.esperarTecla()

if __name__ == "__main__":
    main()
