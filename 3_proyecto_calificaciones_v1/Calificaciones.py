calificaciones=[]

#lista=[
 #  ["Eduardo", 10.0, 10.0, 10.0],
  # ["Joel", 10.0, 9.8, 8.5],
   #["Ruben", 5.0, 6.0, 7.0]
#]

def borrar_pantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t... Oprime  una tecla para continuar...")

def menu_principal():
    print(" \n..::: Sistema de Gestión de Calificaciones :::...\n\n 1.- Agregar \n 2.- Mostrar \n 3.- Calcular Promedio \n 4.- SALIR   ")
    opcion=input("\t Elige una opción (1-4): ")
    return opcion

def agreagar_calificaciones(datos):
   borrar_pantalla()
   print(".:: Añadir Las Calificaciones ::. ")
   nombre=input("Ingresa el nombre del alumno:").upper().strip()
   calif_1=float(input("Ingresa la Calificacion 1:"))
   calif_2=float(input("Ingresa la Calificacion 2:"))
   calif_3=float(input("Ingresa la Calificacion 3:"))












#print("\n\t.:: Agregar Característicaa a  Películas ::\n")
   #atributo= input("Ingresa el nombre del alumno: ").lower() .strip()
   #valor1=input(f"Ingresa la calificacion 1: ").upper().strip()
   #.update({atributo: input(f"Ingrese el valor de la característica '{atributo}': ").upper().strip()})
   #pelicula[atributo] = valor
   #print("\n\t.::¡LA OPERACION SE REALIZO CON EXITO!::.\n") 