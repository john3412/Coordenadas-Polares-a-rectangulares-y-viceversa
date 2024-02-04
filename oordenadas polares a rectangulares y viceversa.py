# Nombre del programa: Coordenadas polares a rectangulares y viceversa
# Descripción: Programa que convierte coordenadas polares a rectangulares y viceversa
# Autor: Jonathan López Ayala
# Fecha: 02/11/2022

import math
import os # Importa funciones compatibles dentro del SO

# Función que muestra el menú de opciones

def Opciones():
    print("\nMenu de opciones\n\n")
    print("\n1. Convertir coordenadas polares a rectangulares.\n")
    print("\n2. Convertir coordenadas rectangualres a polares.\n")
    print("\n3. Salir.\n\n")

    opcion = int(input("Elige una opcion: "))
    #print("Elige una opcion: ")
    #opcion = int(input())
    return opcion

# Función que convierte de grados a radianes
def grados_a_radianes(grados):
    return (grados * math.pi)/180

# Función que convierte coordenadas polares a rectangulares
def polares_a_rectangulares(radio, angulo):
    ar = grados_a_radianes(angulo)

    x = radio * math.cos(ar)
    y = radio * math.sin(ar)

    return x,y

# Función que convierte coordenadas rectangulares a polares
def rectangualares_a_polares(x,y):
    radio = math.sqrt(pow(x, 2)+pow(y, 2))
    angulo = math.atan(y / x)

    return radio, angulo

#Función principal
def main():

    os.system("color 02")
    # Sección de variables, se opta por usar el tipo flotante para ingresar un valor decimal y obtener un resultado del mismo tipo
    x = 0.0
    y = 0.0
    r = 0.0
    ag = 0.0
    x1 = 0.0
    y1 = 0.0
    rad = 0.0
    ang = 0.0

    opcion = 0

    while True:

        opcion = Opciones()

        if opcion == 1:
            print("Convertir de Polar a rectangular\n\n") # Esta cadena de texto indica que función realiza el programa
            r = float(input("Introduce el valor del radio: "))
            ag = float(input("Introduce el valor del angulo: "))

            os.system("cls")

            x,y = polares_a_rectangulares(r,ag)
            print(f"\nEl valor de x en coordenadas rectangulares es: {x}\n") # Muestra el resultado en pantalla
            print(f"El valor de y en coordenadas rectangulares es: {y}\n") # Muestra el resultado en pantalla
            os.system("pause")

        elif opcion == 2:
            print("Convertir de Rectangular a polar\n\n") # Esta cadena de texto indica que función realiza el programa
            x1 = float(input("Introduce el valor de x: "))
            y1 = float(input("Introduce el valor de y: "))

            os.system("cls")

            rad, ang = rectangualares_a_polares(x1,y1)
            print(f"El valor del radio es: {rad} \n")

            if (ang < 0):
                print(f"\nEl valor del angulo es: {ang + math.pi * (180 / math.pi)}° grados\n")
            else:
                print(f"El valor del angulo es: {ang * (180 / math.pi)}° grados\n")
            os.system("pause")

        elif opcion == 3:
            print("Gracias por usar el programa. Hasta pronto.")
            break

        else:
            os.system("cls")
            print("Opcion invalida intente de nuevo \n")
            os.system("pause")

# Llamada a la funcion principal
main()
