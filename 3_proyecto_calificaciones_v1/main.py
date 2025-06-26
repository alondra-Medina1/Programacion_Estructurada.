#Proyecto 3
#Crear un proyecto  que permita  gestionar (administrar) calificaciones, colocar  un menu  de opciones para agregar,  mostrar, calcular promedios 
#de calificaciones de los alumnos y salir
# Notas:

#1.- Utiliza  funciones y mandar a llamar desde otro archivo 
#2.- Utilizar listas  para almacenar  el nombre de un alumno y 3 clasificaciones  
import Calificaciones

def main():

    opcion=True
    datos = []
    while opcion:
        Calificaciones.borra_pantalla()
        opcion=Calificaciones.menu_pricpal()

    match opcion:
        case "1":
            Calificaciones.agrearCalificaciones(datos)
            Calificaciones.esperarTecla()
        case "2":
            Calificaciones.mostrarCalificaciones(datos)
            Calificaciones.esperarTecla() 
        case "3":
           Calificaciones.CalcularPromedios(datos)   
           Calificaciones.esperarTecla()
        case "4":
           opcion=False
           Calificaciones.borra_pantalla() 
           print("Terminaste la ejecucion del SW")
        
        case _:
            opcion=True 
            input("Opción invalida vuelva a intentarlo ... por favor")

main()

if __name__ == "__main__":
    main()