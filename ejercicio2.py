# Realice un programa que lea el código numérico de un producto como llave de un 
# diccionario y en dicha llave va a almacenar nombre, precio y cantidad 
# del producto en una lista.
# El programa debe permitir cargar datos al diccionario, debe mostrar 
# un listado completo del diccionario y debe permitir consultar un producto 
# por su llave.
# CRUD Create, Read, Update, Delete
def crear(productos):
    codigo = int(input('Digite el código del producto\n'))
    descripcion = input('Digite el nombre del producto\n')
    precio = int(input('Digite el precio unitario del producto\n'))
    cantidad = int(input('Digite la cantidad existente del prodcuto\n'))
    productos[codigo] = [descripcion, precio, cantidad]
    return productos
    
def mostrar(productos):
    print('LISTADO DE PRODUCTOS')
    print('Nombre\t\tPrecio\t\tCantidad')
    for i in productos:
        #print(productos[i][0]+'\t\t'+ str(productos[i][1])+'\t\t'+ str(productos[i][2]))
        print(productos[i][0], productos[i][1], productos[i][2], sep="\t\t")

def consultar(productos):
    cod = int(input('Digite el código que desea consultar'))
    if cod in productos:
        print('Nombre\t\tPrecio\t\tCantidad')
        print(productos[cod][0], productos[cod][1], productos[cod][2], sep="\t\t")
    else:
        print('El código del producto no existe')
        

continuar = 's'
productos = {}
while continuar == 's' or continuar == 'S':
    print('MENU')
    print('1. Crear producto')
    print('2. Mostrar productos')
    print('3. Consultar producto ')
    opcion = int(input('Digite una opción del menú [1,2,3]:\n'))
    if opcion == 1:
        crear(productos)
        print(f'El producto ha sido creado con éxito')
        # print(productos)
    elif opcion == 2:
        mostrar(productos)
    elif opcion == 3:
        consultar(productos)
    else:
        print('Digite una opción válida (1, 2 o 3)')
    continuar = input('Digite "s" para continuar o cualquier letra para salir\n')    
    