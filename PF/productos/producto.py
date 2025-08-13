from conexionBD import *

def agregar(codigo,descripcion,marca,precio,cantidad,id_categoria,id_proveedor):
    try:
        cursor.execute("insert into productos (codigo,descripcion,marca,precio,cantidad,id_categoria,id_proveedor) values (%s,%s,%s,%s,%s,%s,%s)",(codigo,descripcion,marca,precio,cantidad,id_categoria,id_proveedor))
        conexion.commit()
        return True
    except:
        return False
    
def mostrar(codigo):
    try:
        cursor.execute("select * from productos where codigo=%s",(codigo,))
        return cursor.fetchall()
    except:
        return []

def modificar(codigo,descripcion,marca,precio,cantidad):
    try:
        cursor.execute("update productos set codigo=%s, descripcion=%s, marca=%s, precio=%s, cantidad=%s where codigo=%s",(codigo,descripcion,marca,precio,cantidad))
        conexion.commit()
        return True
    except:
        return False

def borrar(codigo):
    try:
        cursor.execute("delete from productos where codigo=%s",(codigo,))
        conexion.commit()
        return True
    except:
        return False