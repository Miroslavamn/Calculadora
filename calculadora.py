# Calculadora 

#6 utilizar una librería para ejecutar las operaciones
import numpy as np

#4 Solicitar dos número al usuario
def numeros ():
    global num1, num2
    num1 = float(input("\n Ingresa un número: "))
    num2 = float(input("\n Ingresa otro número: "))

def numero ():
    global num1
    num1 = float(input("\n Ingresa un número: "))

#8 Dividir en funciones
#Función para realizar una suma de dos números
def suma(num1, num2):
    print("\n El resultado es: ", num1+num2)

#Función para realizar una resta de dos números
def resta(num1, num2):
    print("\n El resultado es: ", num1-num2)

#Función para realizar una división de dos números
def multiplicacion(num1, num2):
    print("\n El resultado es: ", num1*num2)

#Función para realizar una multiplicación de dos números
def division(num1, num2):
    if num2 == 0:
        print("\n No es posible dividir entre cero")
    else:
        print("\n El resultado es: ", num1/num2)

#Función para calcular la raiz cuadrada de un número
def raiz(num1):
    print("\n El resultado es: ", np.sqrt(num1))

#Función para calcular el exponente de un número
def exponente(num1):
    print("\n El resultado es: ", np.exp(num1))

#Función para calcular el seno de un número
def seno(num1):
    print("\n El resultado es: ", np.sin(num1))

#Función para calcular el coseno de un número
def coseno(num1):
    print("\n El resultado es: ", np.cos(num1))

#Función para calcular el tangente de un número
def tangente(num1):
    print("\n El resultado es: ", np.tan(num1))

#3 Opción para volver a ejecutar la operación o salir al menú
def repetir(opc):
    
    while 1:
        if opc == 10:
            exit()
            
        x = int(input("\n Elige 1 para volver a ejecutar la misma operación o 2 para regresar al menú principal: "))
        if x == 1:
            operaciones(opc)
        #regresar al menú  
        elif x == 2:
             break
        else:
            print("\n Opción inválida, elige otra \n")

def operaciones(opc):
    if opc == 1:
        numeros()
        suma(num1,num2)
    elif opc == 2:
        numeros()
        resta(num1,num2)
    elif opc == 3:
        numeros()
        multiplicacion(num1,num2)
    elif opc == 4:
        numeros()
        division(num1,num2)
    elif opc == 5:
        numero()
        raiz(num1)
    elif opc == 6:
        numero()
        exponente(num1)
    elif opc == 7:
        numero()
        seno(num1)
    elif opc == 8:
        numero()
        coseno(num1)
    elif opc == 9:
        numero()
        tangente(num1)
    elif opc == 10:
        print("\n Fin..")
    else:
        print("\n Opción inválida \n")

#1 Menú de operaciones disponibles 
while 1:
    print('\n ¿Qué operación quieres realizar?')
    print('1 Suma')
    print('2 Resta')
    print('3 Multiplicación')
    print('4 División')
    print('5 Raiz n')
    print('6 Exponente n')
    print('7 Seno')
    print('8 Coseno')
    print('9 Tangente')
    print('10 Salir')

    opc = int(input('\n Opción: '))
    operaciones(opc)
    repetir(opc)
