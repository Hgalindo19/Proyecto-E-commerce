# Funciones del Carrito

# Listas globales que se recibiran de otro Perfil / RECORDATORIO: Modificar Listas para que coincidan
lista_productos = []
lista_precios = []
lista_stock = []
lista_categorias = []

# Variables del cliente actul
cliente_actual_id = None

# Lista del carrrito del cliente (temporales para cada sesión)
carrito_cliente = []
precios_carrito = []

def inicializar_carrito(id_cliente):
    """Limpia el carrito y asigna ID del cliente"""
    global cliente_actual_id
    cliente_actual_id = id_cliente
    carrito_cliente.clear()
    precios_carrito.clear()
    print("Carrito inicializado para cliente ID: " + str(cliente_actual_id))
    
    

def mostrar_catalogo_completo():
    """
    Muestr el catalogo completo con stock restante.
    """
    if len(lista_productos) == 0:
        print("No hay producs en el catalogo")
        return
        
    print("\nCATALOGO COMPLETO")
    print("-" * 80)
    print("ID  PRODUCTO              CATEGORIA      PRECIO    STOCK RESTANTE")
    print("-" * 80)
    
    i = 0
    while i < len(lista_productos):
        print(str(i) + "  " + lista_productos[i].title() + "  " + 
              lista_categorias[i].title() + "  $" + str(lista_precios[i]) + "    " + str(lista_stock[i]))
        i = i + 1
    
    print("-" * 80)

def menu_carrito():
    """
    Menu interactivo del carrito 
    """
    while True:
        print("\n" + "="*40)
        print("MENÚ CARRITO - Cliente ID: " + str(cliente_actual_id))
        print("="*40)
        print("1. Agregar producto")
        print("2. Ver carrito")
        print("3. Generar ticket")
        print("4. Salir")
        
        opcion = input("\nElige una opcion (1-4): ").strip()
        
        if opcion == "1":
            agregar_producto_carrito()
        elif opcion == "2":
            ver_carrito_y_total()
        elif opcion == "3":
            mostrar_ticket_final()
        elif opcion == "4":
            print("Volviendo al menu principal...")
            break
        else:
            print("Opcion invalida!")
            input("Presiona Enter para continuar...")
            
            
def agregar_producto_carrito():
    """
    Función para agregar productos al carrito del liente
    """
    while True:
        print("\n" + "="*50)
        print("AGREGAR PRODUCTO AL CARRITO")
        print("="*50)
        print("-"*50)
        
        mostrar_catalogo_completo()
        print("-"*50)
        print("Escribe 'SALIR' para volver al menu carrito")
        
        try:
            opcion = input("\nIngresa el ID del producto: ").strip().upper()
            
            if opcion == "SALIR":
                print("Volviendo al menu carrito...")
                return False
            
            id_producto = int(opcion)
            
            if id_producto < 0 or id_producto >= len(lista_productos):
                print("ID invalido!")
                input("Presiona Enter para continuar...")
                continue
                
            if lista_stock[id_producto] <= 0:
                print(f"Producto '{lista_productos[id_producto]}' SIN STOCK")
                input("Presiona Enter para continuar...")
                continue
                
            indices_carrito = [i for i in range(len(carrito_cliente)) if lista_productos[id_producto] in carrito_cliente[i]]
            
            cantidad = int(input(f"Cantidad de '{lista_productos[id_producto]}' (max {lista_stock[id_producto]}): "))
            
            if cantidad <= 0 or cantidad > lista_stock[id_producto]:
                print("Cantidad invalida!")
                input("Presiona Enter para continuar...")
                continue
                
            if len(indices_carrito) > 0:
                indice_existente = indices_carrito[0]
                cantidad_existente_str = carrito_cliente[indice_existente].split('x')[-1].strip(')')
                cantidad_existente = int(cantidad_existente_str)
                nueva_cantidad = cantidad_existente + cantidad
                carrito_cliente[indice_existente] = f"{lista_productos[id_producto]} (x{nueva_cantidad})"
                precios_carrito[indice_existente] = nueva_cantidad * lista_precios[id_producto]
            else:
                carrito_cliente.append(f"{lista_productos[id_producto]} (x{cantidad})")
                precios_carrito.append(cantidad * lista_precios[id_producto])
            
            lista_stock[id_producto] -= cantidad
            
            print(f"'{lista_productos[id_producto]}' agregado al carrito!")
            
            continuar = input("\nAgregar otro producto? (S/N): ").strip().upper()
            if continuar != "S":
                print("Volviendo al menu carrito...")
                return True
                
        except ValueError:
            print("Debes ingresar un numero valido o 'SALIR'!")
            input("Presiona Enter para continuar...")
            
            
def ver_carrito_y_total():
    """
    Muestra el carrito completo con totales finaless.
    """
    print("\n" + "="*60)
    print("MI CARRITO")
    print("="*60)
    
    if len(carrito_cliente) == 0:
        print("Tu carrito esta vacio")
        input("Presiona Enter para continuar...")
        return 0
    
    subtotal = 0
    impuestos = 0
    for precio in precios_carrito:
        subtotal = subtotal + precio
        impuestos = impuestos + (precio * 0.21)
    total_final = subtotal + impuestos
    
    i = 0
    while i < len(carrito_cliente):
        print(str(i+1) + ". " + carrito_cliente[i] + " $" + str(precios_carrito[i]))
        i = i + 1
    
    print("-" * 60)
    print("SUBTOTAL      $" + str(subtotal))
    print("IVA (21%)     $" + str(impuestos))
    print("TOTAL A PAGAR $" + str(total_final))
    print("="*60)
    input("Presiona Enter para continuar...")
    return total_final

def mostrar_ticket_final():
    """
    Genera un ticket prolijo para la salida con ID de cliente.
    """
    if len(carrito_cliente) == 0:
        print("No hay productos para generar ticket")
        input("Presiona Enter para continuar...")
        return
    
    total = ver_carrito_y_total()
    
    print("\n" + " "*70)
    print("TICKET DE COMPRA FINAL")
    print(" "*70)
    
    fecha = "XX/XX/20XX"
    print("Fecha: " + fecha)
    print("Cliente: ID " + str(cliente_actual_id))
    print("-"*70)
    
    i = 0
    while i < len(carrito_cliente):
        print(carrito_cliente[i].upper() + " $" + str(precios_carrito[i]))
        i = i + 1
    
    print("-"*70)
    print("TOTAL $" + str(total))
    print("\n" + " "*70)
    print("GRACIAS POR SU COMPRA")
    print(" "*70)
    
    carrito_cliente.clear()
    precios_carrito.clear()
    print("Carrito vaciado correctamente")
    input("Presiona Enter para continuar...")

# Ejemplo de uso (para probar que funcione todo): 
if __name__ == "__main__":
    lista_productos = ["Objeto 1", "Objeto 2", "Objeto 3", "Objeto 4"]
    lista_precios = [150.5, 80.0, 200.0, 120.0]
    lista_stock = [10, 5, 3, 8]
    lista_categorias = ["Categoria 1", "Categoria 2", "Categoria 3", "Categoria 4"]
    
    inicializar_carrito(123)
    menu_carrito()
    
    
