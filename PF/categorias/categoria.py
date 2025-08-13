from conexionBD import *

def agregar(nombre_categoria):
    try:
        cursor.execute("INSERT INTO categorias_productos (nombre_categoria) VALUES (%s)", (nombre_categoria,))
        conexion.commit()
        return True
    except Exception as e:
        print("❌ Error:", e)
        return False
    
def mostrar(nombre_categoria):
    try:
        cursor.execute("select * from notas where nombre_categoria=%s",(nombre_categoria,))
        return cursor.fetchall()
    except:
        return []