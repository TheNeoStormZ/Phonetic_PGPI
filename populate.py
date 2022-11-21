import sqlite3
import random
nombre_db = "db.sqlite3"
secciones_list = ["Huawei","Xiaomi","Vivo","Samsung","Desconocido"]
categoria_list = ["Funda", "Cargadores", "Protectores","Otros"]

def popular_db(elemnts=3):
    conn = sqlite3.connect(nombre_db)
    for i in range (0,elemnts):
        nombre = "Nombre" + str(i+1)
        descripcion = "Una descripcion epica nº" + str(i+1)
        element = random.randint(0, 3)
        categoria = categoria_list[element]
        element = random.randint(0, 4)
        secciones = secciones_list[element]
        precio = float((i+1)*4)
        imagen = "http://atlas-content-cdn.pixelsquid.com/stock-images/generic-smartphone-63AoDxD-600.jpg"
        stock = int(i)
        conn.execute("""INSERT INTO principal_producto (nombre, descripcion, imagen, stock, categoria,secciones,precio) VALUES (?,?,?,?,?,?,?)""",
                    (nombre, descripcion, imagen, stock, categoria, secciones,precio))
    conn.commit()
    conn.close()

popular_db(10)

