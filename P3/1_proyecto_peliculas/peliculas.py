import mysql.connector
from mysql.connector import Error

pelicula={}

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t🌟... Oprime una tecla para continuar... 🎬")

def conectar():
    try:
        conexion = mysql.connector.connect(
          host="localhost",
          user="root",
          password="", 
          database="bd_peliculas"
        )
        return conexion
    except Error as e:
        print(f"El error que se presenta es: {e}")
        return None

def crearPeliculas():
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t🎥 .:: Crear Películas :: 🍿\n")
        pelicula["nombre"]=input("Ingrese el nombre:").upper().strip()
        #pelicula.update({"nombre":input("🎞️ Ingrese el nombre: ").upper().strip()})
        pelicula.update({"categoria":input("📂 Ingrese la categoría: ").upper().strip()})
        pelicula.update({"clasificacion":input("🔖 Ingrese la clasificación: ").upper().strip()})
        pelicula.update({"genero":input("🎭 Ingrese el género: ").upper().strip()})
        pelicula.update({"idioma":input("🗣️ Ingrese el idioma: ").upper().strip()})
        
        #####BD
        cursor=conexionBD.cursor()
        sql="insert into peliculas (nombre,categoria,clasificacion,genero,idioma)value (%s,%s,%s,%s,%s)"#%s es para representar nombre etc, siemte tiene que ser en  orden 
        val=(pelicula["nombre"],pelicula["categoria"],pelicula["clasificacion"],pelicula["genero"],pelicula["idioma"])
        cursor.execute(sql,val)
        conexionBD.commit()#El commit es para ver que todo funcione correctamente
        print("\n\t\t✅ .::¡LA OPERACIÓN SE REALIZÓ CON ÉXITO!:: ✅")

def mostrarPeliculas():
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t📺 .:: Mostrar Películas ::. 📺\n")
        cursor=conexionBD.cursor()
        sql="select * from peliculas"
        cursor.execute(sql)
        registros=cursor.fetchall()#Todo lo que hay en la tabla te lo regresa en una lista y los entrega en una lista 
        if registros:
            print("Mostrar las Peliculas")
            print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
            print(f"-"*80)
            for pelis in registros:
                print(f"{pelis[0]:<10}{pelis[1]:<15}{pelis[2]:<15}{pelis[3]:<15}{pelis[4]:15}{pelis[5]:<15}")
                print(f"-"*80)
        else:
            print("\t📭 .:: No hay películas en el sistema ::.")

def buscarPeliculas():
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
      print("\n\t.:: Buscar Películas ::. \n")
      nombre=input("Ingresa el nombre de la pelicula a buscar: ").upper().strip()
    cursor=conexionBD.cursor()
    sql="select * from peliculas where nombre=%s"
    val=(nombre,)
    cursor.execute(sql,val)
    registros=cursor.fetchall()
    if registros:
      print("Mostrar las Peliculas")
      print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
      print(f"-"*80)
      for pelis in registros:
        print(f"{pelis[0]:<10}{pelis[1]:<15}{pelis[2]:<15}{pelis[3]:<15}{pelis[4]:<15}{pelis[5]:<15}")
      print(f"-"*80)  
    else:
      print("\t .:: peliculas no encontradas en el sistema ::..")

def borrarPeliculas():
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
      print("\n\t.:: Borrar Películas ::. \n")
      nombre=input("Ingresa el nombre de la pelicula a borrar: ").upper().strip()
      cursor=conexionBD.cursor()
      sql="select * from peliculas where nombre=%s"
      val=(nombre,)
      cursor.execute(sql,val)
      registros=cursor.fetchall()
      if registros:
         print("Mostrar las Peliculas")
         print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
         print(f"-"*80)
         for pelis in registros:
            print(f"{pelis[0]:<10}{pelis[1]:<15}{pelis[2]:<15}{pelis[3]:<15}{pelis[4]:<15}{pelis[5]:<15}")
            print(f"-"*80)  
            respuesta=input("¿Deseas borrar la pelicula {nombre}? (Si/No):").lower().strip()
            if respuesta=="si":
               sql="delete from peliculas where nombre =%s"
               val=(nombre,)
               cursor.execute(sql,val)
               conexionBD.commit()
               print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON EXÍTO! :::")
      else:
         print("\t .:: peliculas no encontradas en el sistema ::..")

def modificarPeliculas():
  borrarPantalla()
  conexionBD = conectar()
  if conexionBD != None:
    nombre = input("Ingresa el nombre de la película a modificar: ").upper().strip()
    cursor = conexionBD.cursor()
    sql = "SELECT * FROM peliculas WHERE nombre = %s"
    val = (nombre,)
    cursor.execute(sql, val)
    registros = cursor.fetchall()
    
    if registros:
      print("Película encontrada:")
      print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
      print(f"-" * 80)
      for pelicula in registros:
        print(f"{pelicula[0]:<10}{pelicula[1]:<15}{pelicula[2]:<15}{pelicula[3]:<15}{pelicula[4]:<15}{pelicula[5]:<15}")
      print(f"-" * 80)

      print("\nIngresa los nuevos datos (deja en blanco si no deseas modificar ese campo):")
      nuevo_nombre = input("Nuevo nombre: ").upper().strip()
      nueva_categoria = input("Nueva categoría: ").upper().strip()
      nueva_clasificacion = input("Nueva clasificación: ").upper().strip()
      nuevo_genero = input("Nuevo género: ").upper().strip()
      nuevo_idioma = input("Nuevo idioma: ").upper().strip()

      # Obtener los datos actuales si el usuario deja un campo vacío
      actual = registros[0]
      if not nuevo_nombre:
        nuevo_nombre = actual[1]
      if not nueva_categoria:
        nueva_categoria = actual[2]
      if not nueva_clasificacion:
        nueva_clasificacion = actual[3]
      if not nuevo_genero:
        nuevo_genero = actual[4]
      if not nuevo_idioma:
        nuevo_idioma = actual[5]

      sql = "UPDATE peliculas SET nombre = %s, categoria = %s, clasificacion = %s, genero = %s, idioma = %s WHERE id = %s"
      val = (nuevo_nombre, nueva_categoria, nueva_clasificacion, nuevo_genero, nuevo_idioma, actual[0])
      cursor.execute(sql, val)
      conexionBD.commit()
      print("\n\t::: ¡LA MODIFICACIÓN SE REALIZÓ CON ÉXITO! :::")
    else:
      print("\n\t..:: La película no fue encontrada en el sistema ::..")

