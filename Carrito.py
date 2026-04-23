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