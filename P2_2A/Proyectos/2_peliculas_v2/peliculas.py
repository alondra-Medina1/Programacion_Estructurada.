#dict u objeto para al,acenar los atrivutos( nombre, categoria, clasificacion, genero, idioma)

#pelicula=¨{
#      "nombre",
#      "categoria":"",
#     "clasificacion":"",
#        "genero":"",
#        "idioma":""
#}

pelicula={}


def borra_pantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t... Oprime  una tecla para continuar...")
    
def crear_peliculas():
    borra_pantalla()
    print("\n\t.:: Alta de Películas ::\n")
    pelicula.update({"nombre":input("Ingrese el nombre: ").upper ().strip ()})
    pelicula.update({"categoria":input("Ingrese la categoria: ").upper ().strip ()})
    pelicula.update({"clasificacion":input("Ingrese la clasificacion: ").upper ().strip ()})
    pelicula.update({"genero":input("Ingrese el genero: ").upper ().strip ()})
    pelicula.update({"idioma":input("Ingrese el idioma: ").upper ().strip ()})
    print("\n\t.::¡LA OPERACION SE REALIZO CON EXITO!::.")

def mostrarPeliculas():
    borra_pantalla()
    print("\n\t.:: Consultar la  Película ::\n")
    if len(pelicula) > 0:
       for i in pelicula:
           print(f"\t{i}: {pelicula[i]}")
    else:
       print("\t.::No hay películas en el sistema.")

def borrar_peliculas():
     borra_pantalla()
     print("\n\t.:: Borrar o quitar TODAS las  Películas ::\n")
     resp=input("¿Desas quitar o borrar todas las películas del sistema? (si/No): ")
     if resp== "si":   
      pelicula.cls()
      print("\n\t.::¡LA OPERACION SE REALIZO CON EXITO!::.")  

def agreagarCaracteristicaPeliculas():
   borra_pantalla()
   print("\n\t.:: Agregar Característicaa a  Películas ::\n")
   atributo= input("Ingrese la nueva característica de la película: ").lower() .strip()
   valor=input(f"Ingrese el valor de la característica de la pelicula: ").upper().strip()
   pelicula.update({atributo: input(f"Ingrese el valor de la característica '{atributo}': ").upper().strip()})
   pelicula[atributo] = valor
   print("\n\t.::¡LA OPERACION SE REALIZO CON EXITO!::.\n") 

def modificarCaracteristcaPeliculas():
    borra_pantalla()
    print("\n\t.:: Modificar Característicaa de Películas ::\n")
    atributo = input("Ingrese el nombre de la característica a modificar: ").lower().strip()
    if atributo in pelicula:
        nuevo_valor = input(f"Ingrese el nuevo valor para '{atributo}': ").upper().strip()
        pelicula[atributo] = nuevo_valor
        print(f"\n\t.::¡La característica '{atributo}' se ha modificado con éxito!::.\n")
    else:
        print(f"\n\t.::¡La característica '{atributo}' no existe en la película!::.\n")
    print("\n\t.::¡LA OPERACION SE REALIZO CON EXITO!::.\n")

def borrarCaracteristicaPeliculas():
    borra_pantalla()
    print("\n\t.:: Borrar Características de la  Película ::\n")
    atributo = input("Ingrese el nombre de la característica a borrar: ").lower().strip()
    if atributo in pelicula:
        del pelicula[atributo]
        print(f"\n\t.::¡La característica '{atributo}' se ha borrado con éxito!::.\n")
    else:
        print(f"\n\t.::¡La característica '{atributo}' no existe en la película!::.\n")
    print("\n\t.::¡LA OPERACION SE REALIZO CON EXITO!::.\n")
     
