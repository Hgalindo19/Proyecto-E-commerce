"""Perimitir busqueda de Items por ID"""
Productos= {
    1001: {"Nombre": "Notebook", "Precio":600000, "Categoria": "Computacion", "Stock":10},
    1002: {"Nombre": "Monitor", "Precio": 675000, "Categoria": "Monitores", "Stock":5},
    1003: {"Nombre": "Auriculares", "Precio": 200000, "Categoria": "Audio", "Stock": 20},
    1004: {"Nombre": "Teclado", "Precio": 30000, "Categoria": "Perifericos", "Stock": 15},
}
def agregar_productos(id_prod,nombre,precio,categoria,stock):
    Productos[id_prod]= {
"Nombre": nombre,
"Precio": precio,
"Categoria": categoria,
"Stock": stock
    }