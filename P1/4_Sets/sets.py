#Set es una coleccion desordenada 
  #Los sets se utilizan para almacenar cosas

import os

os.system("cls")
paises=["Mexico", "España", "Canada", "Brasil"]
print(paises)

#Funciones u operaciones 
for i in paises:
    print(i)

#paises.add("México")
#print(paises)

paises.pop()
print(paises)

#   Es para remover algun valolr 
paises.remove("Mexico")
print(paises)

os.system("cls")
#Ejemplo crear un programa que solicite los email de los alumnos de la UTD almacenar en la lista
#y posteriormente mostrar en pantalla los email sin duplicados

emails=[]
resp="si"

while resp=="si":
    emails.append(input("Ingrese un email de la UTD"))
    resp=input("¿Deseas ingresar otro email?").lower()

emails_set=set(emails)
emails=list(emails_set)
