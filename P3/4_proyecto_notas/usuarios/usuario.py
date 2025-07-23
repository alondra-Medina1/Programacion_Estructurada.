from conexionBD import * 
import datetime
import hashlib

def hash_password(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def registrar(nombre, apellidos, email, password):
    try:
        fecha = datetime.datetime.now()
        contrasena = hash_password(password)  # Corregido aquí
        sql = "INSERT INTO usuarios (nombre, apellidos, email, password, fecha) VALUES (%s, %s, %s, %s, %s)"
        val = (nombre, apellidos, email, contrasena, fecha)
        cursor.execute(sql, val)
        conexion.commit()
        return True
    except Exception as e:
        print("Error en el registro:", e) 
        return False

def inicio_sesion(email, contrasena):
    try:
        contrasena = hash_password(contrasena)
        sql = "SELECT id, nombre, apellidos FROM usuarios WHERE email = %s AND password = %s"
        val = (email, contrasena)
        cursor.execute(sql, val)
        registro = cursor.fetchone()
        if registro:
            return registro  
        else:
            return None
    except Exception as e:
        print("Error al iniciar sesión:", e)
        return False