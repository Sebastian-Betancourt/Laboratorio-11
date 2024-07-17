import random

datosBiometrico = [[], [], []]

def mostrar_menu_principal():
    print("--------------- SISTEMA BIOMETRICO -------------")
    print("-------------------Bienvenido -------------------")
    print("¿Qué acción desea realizar?: ")
    print('*  1) Login')
    print('*  2) Registro de usuarios')
    print('*  3) Buscar usuario')
    print('*  4) Salir del sistema')
    return obtener_opcion([1, 2, 3, 4])

def obtener_opcion(opciones_validas):
    while True:
        try:
            opcion = int(input("Ingrese la opción: "))
            if opcion in opciones_validas:
                return opcion
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor ingrese un número entero.")

def login():
    if len(datosBiometrico[0]) == 0:
        print("No existen usuarios registrados")
    else:
        user = input("Ingrese el rostro de la persona en la cámara: ")
        if user in datosBiometrico[1]:
            print('-------- Bienvenido ----------')
            print("----- Módulos disponibles -------")
            print("¿Qué acción desea realizar?: ")
            print('*  4) Cerrar sesión')
            return obtener_opcion([4])
        else:
            print("No existe el usuario")
    return mostrar_menu_principal()

def registro_usuarios():
    print("¿Qué acción desea realizar?: ")
    print('*  1) Ingresar usuarios')
    print('*  2) Mostrar usuarios')
    print('*  3) Salir al menú principal')
    tipoAccion=obtener_opcion ([1, 2, 3])

    while tipoAccion !=3:
        if tipoAccion ==1:
            ingresar_usuarios()
        elif tipoAccion== 2:
            mostrar_usuarios()
        tipoAccion=mostrar_menu_registro()
    return mostrar_menu_principal()

def ingresar_usuarios():
    while True:
        try:
            numPersonas = int(input("Ingrese el número de personas a registrar (1-20): "))
            if 1 <= numPersonas<= 20:
                break
            else:
                print("Número fuera de rango. Intente de nuevo. ")
        except ValueError:
            print("Entrada no válida. Por favor ingrese un número entero positivo. ")

    for i in range(numPersonas):
        while True:
            nombreUsuario = input("Nombre de la persona: ")
            if nombreUsuario.isalpha():
                break
            else:
                print("El nombre no debe contener números. Intente de nuevo. ")
        huellaUsuario =input("Huella facial: ")
        datosBiometrico[0].append(nombreUsuario)
        datosBiometrico[1].append(huellaUsuario)
        datosBiometrico[2].append(random.randrange(1000, 9999))

def mostrar_usuarios():
    for i in range(len(datosBiometrico[0])):
        print("-------------------------------------")
        print("Mostrando los datos de la persona", i + 1)
        print("* Nombre:", datosBiometrico[0][i])
        print("* Huella dactilar:", datosBiometrico[1][i])
        print("* Código de acceso: ", datosBiometrico[2][i])
        print("-------------------------------------")

def buscar_usuario():
    if len(datosBiometrico[0]) == 0:
        print("No existen usuarios registrados ")
    else:
        nombreUsuario = input("Ingrese el nombre del usuario a buscar: ")
        if nombreUsuario in datosBiometrico[0]:
            index = datosBiometrico[0].index(nombreUsuario)
            print("-------------------------------------")
            print("Datos del usuario buscado")
            print("* Nombre:", datosBiometrico[0][index])
            print("* Huella dactilar:", datosBiometrico[1][index])
            print("* Código de acceso: ", datosBiometrico[2][index])
            print("-------------------------------------")
        else:
            print("Usuario no encontrado")

def mostrar_menu_registro():
    print("¿Qué acción desea realizar?: ")
    print('*  1) Ingresar usuarios')
    print('*  2) Mostrar usuarios')
    print('*  3) Salir al menú principal')
    return obtener_opcion([1, 2, 3])

def sistema_biometrico():
    tipo = mostrar_menu_principal()

    while tipo !=4:
        if tipo ==1:
            tipo =login()
        elif tipo ==2:
            tipo =registro_usuarios()
        elif tipo ==3:
            buscar_usuario()
            tipo = mostrar_menu_principal()

    print("Muchas gracias")

sistema_biometrico()
