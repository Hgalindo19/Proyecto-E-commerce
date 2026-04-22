"""Creacion del Inventario con busqueda por ID"""
lista_producto=[]
lista_precios=[]
lista_stock=[]
lista_categoria=[]
def alta_producto():
    print("Agrege un nuevo producto")
    nombre=input ("Nombre del producto: ")
    categoria= input ("Catergoria: ")
    while True:
        try:
            precio = float(input("Precio: "))
            if precio > 0:
                break
            else:
                print("El precio no debe ser negativo. Intente denuevo")
        except ValueError:
            print("Ingrese un numero valido.")
    
    lista_producto.append(nombre)
    lista_precios.append(precio)
    lista_stock.append(stock)
    lista_categoria.append(categoria)
                


def Agregar_producto(id_producto,nombre,stock,precio,categoria):
    productos[id_producto]= {
        "Nombre": nombre,
        "Precio": precio,
        "Categoria": categoria,
        "Stock": stock
    }

"""""Objetivo: Actualizar Precios de forma masiva 
    Parametro: Precios, Iva
    Salido: Precios Actualizados"""
def actualizar_precios():
    print("Actualizacion de Precios")

while True:
    try:
        porcentaje = float(input("Ingrese cuanto quiere aumentar: "))
        confirmar= input("¿Aplicar? {porcentaje}% a todos los precios (s/n): ").lower()
        if confirmar == "s":
            for i in range(len())