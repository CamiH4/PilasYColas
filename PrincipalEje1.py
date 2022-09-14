import Ejercicio1 as ej
import os

cola = ej.ColaDePacientes()

def encolar():
    print("Escriba los datos del paciente")
    nom = input("Nombre: " )
    ape = input("Apellidos: ")
    pac = ej.ColaDePaciente(nom, ape)
    cola.encolar(pac)
    print("Agregado al registro")

def desencolar():
    print(cola.desencolar(cola.elementos))

def mostrarCola():
    if cola.estaVacia():
        print("registro vacio...")
    else:
        for pac in cola.elementos:
            print(pac)
def menu():
    try:
        print("1. Registrar")
        print("2. Remover")
        print("3. Mostrar registro")
        print("4. Salir")
        op = int(input("Ingrese un opción: "))
        os.system('cls')
        return op
    except Exception as ex:
        raise ValueError(str(ex))

def main():
    op = 0
    while(op != 4):
        print("Bienvenidos - Registro de Pacientes")
        op = menu()
        if(op == 1): encolar()
        elif(op == 2): desencolar()
        elif(op == 3): mostrarCola()
        elif(op == 4): print("Adios...")
        else: print("Opcion invalida...")

main()