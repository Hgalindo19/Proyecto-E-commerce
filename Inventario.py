
lista_producto=[]
lista_precios=[]
lista_stock=[]
lista_categoria=[]

def alta_producto():
    """Objetivo: Crear el Inventario
    Parametro: listas para la creacion del inventario
    Salida: Inventario hecho"""
   
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
    while True:
        try:
            stock=int(input("Stock incial: "))
            if stock >= 0:
                break
            else:
                print("El stock no puede ser negativo")
        except ValueError:
            print("Ingrese un numero entero valido.")
    lista_producto.append(nombre)
    lista_precios.append(precio)
    lista_stock.append(stock)
    lista_categoria.append(categoria)
                
def actualizar_precios():
    """""Objetivo: Actualizar Precios de forma masiva 
    Parametro: sin parametro
    Salido: Precios Actualizados"""
   
    print("Actualizacion de Precios")

    while True:
        try:
            porcentaje = float(input("Ingrese cuanto quiere aumentar: "))
            confirmar= input("¿Aplicar? {porcentaje}% a todos los precios (s/n): ").lower()
            if confirmar == "s":
                for i in range(len(lista_precios)):
                    nuevo_precio= lista_precios[i+ porcentaje/100]
                    lista_precios[i]= int(nuevo_precio)
                print("Precios Actualizados")
                break
            else:
                print("Operacion Cancelada")
        except ValueError:
            print("Ingrese un numero valido.")
            
"""""Objetivo: busqueda de productos con bajo stock
    Parametro: sin parametro
    Salida: busqueda de producto critico"""
def producto_critico():
    print("-"*50)
    print("Productos critico (Bajo)")
    limite=int(input("Mostar productos con stock menor a: "))
    encontrado= False
    for i in range(len(lista_stock)):
        if lista_stock[i] < limite:
            print(f"{i<3},{lista_producto[i]<20} {lista_stock[i]<5} & {lista_precios[i]<11}")
            encontrado=True
        if not encontrado:
            print("Todos los productos tienen stock suficiente")
        print("-"*50)