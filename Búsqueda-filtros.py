# Listas

productos = ["Remera", "Celular", "Auto"]
categorias = ["Ropa", "Tecnología", "Vehículos"]
precios = [15000, 250000, 800000]

# Función mostrar productos

def mostrar_productos():
    for i in range(3):
        print(productos[i], categorias[i], precios[i])
        
# Función buscar categoría

def buscar_categoria():
    
    buscar = input("Ingrese categoría: ")
    
    for i in range(3):
        if buscar == categorias[i]:
            print(productos[i], precios[i])
            
            
# Menú

def menu():
    
    opcion = 0
    
    while opcion != 3:
        
        print("1 - Ver productos")
        print("2 - Buscar categoría")
        print("3 - Salir")
        
        opcion = int(input("Ingrese opción: "))
        
        if opcion == 1:
            mostrar_productos()
            
        elif opcion == 2:
            buscar_categoria()
            
menu()
