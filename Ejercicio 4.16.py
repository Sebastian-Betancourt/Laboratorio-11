
#EJERCICIO 4.16 

def mostrar_menu():
    print("\nMenú de Opciones")
    print("1. Ingresar números")
    print("2. Calcular e impsalirrimir cubos")
    print("3. Salir")

def ingresar_numeros():
    numeros = []
    while True:
        numero = input("Ingrese un número natural positivo (o 'fin' para terminar): ")
        if numero.lower() == 'fin':
            break
        elif numero.isdigit() and int(numero) > 0:
            numeros.append(int(numero))
        else:
            print("Entrada no válida. Por favor, ingrese un número natural positivo.")
    return numeros

def calcular_cubos(numeros):
    cubos = [numero ** 3 for numero in numeros]
    return cubos

def imprimir_cubos(cubos):
    print("\nLos cubos de los números ingresados son:")
    for cubo in cubos:
        print(cubo)

def main():
    numeros = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            numeros = ingresar_numeros()
        elif opcion == '2':
            if numeros:
                cubos = calcular_cubos(numeros)
                imprimir_cubos(cubos)
            else:
                print("No ha ingresado ningún número. Por favor, ingrese números primero.")
        elif opcion == '3':
            print("Gracias por participar.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()
