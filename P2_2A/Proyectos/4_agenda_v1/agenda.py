agenda=[]
agenda={}
def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t... Oprime  una tecla para continuar...")

def menu_principal():
    print("\n\t 📝..::: Sistema de Gestión de Agenda de Contactos  :::... 📝\n\n 1️⃣ Agregar contacto \n 2️⃣ Mostrar todos los contactos \n 3️⃣ Buscar contacto por nombre  \n 4.- SALIR ")
    opcion=input("\t Elige una opción (1-4):  ").upper()
    return opcion

def agregar_contacto():
   borrarPantalla()

def mostrar_contacto():
   borrarPantalla()
   
def buscar_contacto():
    borrarPantalla()
