import Ejercicio2 as e
import os
lib = e.Pila()


def menu():
    try:
        print("1. Agregar")
        print("2. Remover")
        print("3. Mostrar")
        print("4. Salir")
        op = int(input("Digite una opción: "))
        os.system('cls')
        return op
    except Exception as ex:
        raise ValueError(str(ex))


def agregarLib():
    try:
        tit = input("Título: ")
        lib.apilar(tit)
        aut = input("Autor: ")
        lib.apilar(aut)
        ed = input("Edición: ")
        lib.apilar(ed)
        print("Agregado...")
    except Exception as ex:
        return ValueError(str(ex))


def quitarLib():
    print(lib.desapilar)


def mostrar():
    if (lib.esVacia()):
        print("No hay ningun libro.")
    else:
         cont = len(lib.datos)-1
         print("="*10)
         while(cont >= 0):
            num = lib.datos[cont]
            print(num)
            print("="*10)
            cont -= 1

def main():
    op = 0 
    while (op != 4):
        op = menu()
        if op == 1: agregarLib()
        elif op == 2: quitarLib()
        elif op == 3: mostrar()
        elif op == 4:print("Adios...")
        else:
            print("Opcion invalida...")

main()