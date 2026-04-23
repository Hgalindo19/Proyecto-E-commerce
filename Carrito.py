# Funciones del Carrito

# Listas globales que se recibiran de otro Perfil / RECORDATORIO: Modificar Listas para que coincidan
lista_productos = []
lista_precios = []
lista_stock = []
lista_categorias = []

# Variables del cliente actual
cliente_actual_id = None

# Lista del carrito del cliente (temporales para cada sesión)
carrito_cliente = []
precios_carrito = []

def inicializar_carrito(id_cliente):
    """Limpia el carrito y asigna ID del cliente"""
    global cliente_actual_id
    cliente_actual_id = id_cliente
    carrito_cliente.clear()
    precios_carrito.clear()
    print("Carrito inicializado para cliente ID: " + str(cliente_actual_id))