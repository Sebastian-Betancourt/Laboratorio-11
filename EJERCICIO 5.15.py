#EJERCICIO 5.15

def mostrar_menu():
    print("\nMenú de Opciones")
    print("1. Ingresar matriz")
    print("2. Contar elementos negativos")
    print("3. Contar ceros en la diagonal principal")
    print("4. Salir")

def ingresar_matriz():
    matriz = []
    for i in range(5):
        fila = []
        for j in range(6):
            while True:
                try:
                    valor = float(input(f"Ingrese el elemento [{i+1}, {j+1}]: "))
                    fila.append(valor)
                    break
                except ValueError:
                    print("Entrada no válida. Por favor, ingrese un número.")
        matriz.append(fila)
    return matriz

def contar_negativos(matriz):
    negativos = 0
    for fila in matriz:
        for elemento in fila:
            if elemento < 0:
                negativos += 1
    return negativos

def contar_ceros_diagonal(matriz):
    ceros_diagonal = 0
    for i in range(min(len(matriz), len(matriz[0]))):
        if matriz[i][i] == 0:
            ceros_diagonal += 1
    return ceros_diagonal

def main():
    matriz = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            matriz = ingresar_matriz()
        elif opcion == '2':
            if matriz:
                negativos = contar_negativos(matriz)
                print(f"Cantidad de elementos negativos: {negativos}")
            else:
                print("No ha ingresado ninguna matriz. Por favor, ingrese una matriz primero.")
        elif opcion == '3':
            if matriz:
                ceros_diagonal = contar_ceros_diagonal(matriz)
                print(f"Cantidad de ceros en la diagonal principal: {ceros_diagonal}")
            else:
                print("No ha ingresado ninguna matriz. Por favor, ingrese una matriz primero.")
        elif opcion == '4':
            print("Usted salio del programa, gracias.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()
