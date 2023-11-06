import mysql.connector
def conectar(): 
    # Conectar a la base de datos
    conexion = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="mibasededatos",
    port='3306'
    )
    return conexion


def AgregarProducto(Nombre, Stock, Precio):
    conexion = conectar()
    # Crea un cursor para ejecutar consultas SQL
    cursor = conexion.cursor()
    # Sentencia SQL para insertar una tarea en la tabla
    instruccion = "INSERT INTO Productos (Nombre, Stock, Precio,Ventas) VALUES (%s, %s, %s,1);"
    


    # Valores para la instrucción SQL
    valores = (Nombre, Stock, Precio)
    
    # Ejecuta la sentencia SQL con los valores proporcionados
    cursor.execute(instruccion, valores)
    
    # Guarda los cambios en la base de datos
    conexion.commit()
    cursor.close()
    conexion.close()

def ObtenerTablaProductos():
    conexion = conectar()
    cursor = conexion.cursor()  
    cursor.execute("SELECT * FROM Productos")
    productos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return productos


def BorrarProducto(id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Productos WHERE ID_Producto = %s", (id,))
    conexion.commit()
    cursor.close()
    conexion.close()


