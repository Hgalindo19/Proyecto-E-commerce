"""Creacion del Inventario con busqueda por ID"""
productos = {
    1: {"Nombre": "Monitor", "Precio": 250000, "Stock": 6},
    2: {"Nombre": "Teclado Mecanico", "Precio": 45000, "Stock": 20},
    3: {"Nombre": "Mouse","Precio": 20000, "Stock": 10},
    4: {"Nombre": "Auriculares","Precio": 35000, "Stock":15}
}

def Agregar_producto(id_producto,nombre,stock,precio):
    productos[id_producto]= {
        "Nombre": nombre,
        "Precio": precio,
        "Stock": stock
    }
    