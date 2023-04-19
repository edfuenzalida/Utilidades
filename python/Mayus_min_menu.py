# Version 1
# Fecha 18.04.2023
# by edrox
# Descrpción:
#   Menú que cotiene algunas herramientas como:
#       Transformar texto a minusculas y otro a mayusculas


import time
import os

def mostrar_menu(opciones):
    print('Seleccione una opción: ')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, volver a intentar')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()                                     # Se imprime una linea en blanco para dar claridad de lectura 

def menu():
    opciones = {
        '1': ('Convertir a mayuscula', one),
        '2': ('Convertir a minuscula', two),
        '3': ('salir', exit)
    }

    generar_menu(opciones, '3')

def time_clear():
    time.sleep(4)
    os.system("clear")

def one():
    print()
    mi = input("Ingresar texto a transformar: ")
    print()
    print("El texto ingresado en minuscula: ", mi.upper())
    time_clear()
        

def two():
    print()
    ma = input("Ingresar texto a transformar: ")
    print()
    print("El texto ingreado en mayuscula: ", ma.lower())
    time_clear()

def exit():
    print()
    print("Hasta luego... :3 ")

if __name__ == '__main__':
    menu()








