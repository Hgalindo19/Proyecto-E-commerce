import os

def limpiar_pantalla():
    '''Objetivo: limpiar la terminal 
       Parametros: ninguno
       Salida: terminal limpia
       '''
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def leer_entero(mensaje):
    '''Objetivo: verificar que lo ingrersado por el usuario sea un numero entero
       Parametros: un valor x que haya ingresado el usuario
       Salida: un numero entero
       '''
    valor= input(mensaje)
    
    while not valor.isdigit():
       
        print("ERROR, por favor ingrese una opción valida")
        valor= input(mensaje)
    
    return int(valor)
    
def menu_admin():
    '''Objetivo: mostrar el menu del administrador
       Parametros: ninguno
       Salida: menu del administrador
    '''
    continuar= True
    
    while continuar:
        limpiar_pantalla()
        
        print("------------------------------------------")
        print("            MENU ADMINISTRADOR            ")
        print("------------------------------------------\n")
        print("1 --> Gestión de Inventario\n2 --> Salir")
        
        opcion= leer_entero("Selecione una opción: ")
        
        if opcion == 1:
            print("gestion inventario")
            
        elif opcion == 2:
            continuar=False
        
        else:
            print("Opción Invalida")
            
def menu_cliente():
    '''Objetivo: mostrar el menu del usuario
       Parametros: ninguno
       Salida: menu del usuario
    '''
    continuar= True
    
    while continuar:
        limpiar_pantalla()
        
        print("------------------------------------------")
        print("               MENU CLIENTE               ")
        print("------------------------------------------\n")
        print("1 --> Catálogo Completo\n2 --> Búsqueda por Categoria\n3 --> Agregar Producto al Carrito\n4 --> Ver Carrito y Total\n5 --> Salir")
        
        opcion= leer_entero("Seleccione una opción: ")
        
        if opcion == 1:
            print("catalogo")
        
        elif opcion == 2:
            print("busqueda")
            
        elif opcion == 3:
            print("agregar carrito")
            
        elif opcion == 4:
            print("Ver carrito")
        
        elif opcion == 5:
            continuar= False
            
        else:
            print("Opción Invalida")
            
def main():
    '''Objetivo: mostrar el programa funcional
       Parametros: ninguno
       Salida: programa principal funcional
    '''
    continuar= True  
    
    while continuar:
        limpiar_pantalla()
          
        print("------------------------------------------")
        print("           E-COMMERCE BETA 1.O            ")
        print("------------------------------------------\n")
        print("1 --> Ingresar como Administrador\n2 --> Ingresar como Cliente\n3 --> Salir")
        
        opcion= leer_entero("Seleccione una opción: ")
        
        if opcion == 1:
            menu_admin()
        
        elif opcion == 2:
            menu_cliente()
            
        elif opcion == 3:
            continuar=False
            print("Gracias por confiar en nosotros, vuelva pronto")
        
        else:
            print("Opción Invalida")
        
main()