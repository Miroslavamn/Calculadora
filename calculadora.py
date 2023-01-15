# Calculadora 

#Librería para utilizar...
import numpy as np

#Crear función para solicitar números al usuario
def numeros ():
    global num1, num2
    num1 = float(input("\n Ingresa un número: "))
    num2 = float(input("\n Ingresa otro número: "))

#Función para realizar una suma de dos números
def suma(num1, num2):
    print("El resultado es: ", num1+num2)

#Función para realizar una resta de dos números
def resta(num1, num2):
    print("El resultado es: ", num1-num2)

#Función para realizar una división de dos números
def multiplicacion(num1, num2):
    print("El resultado es: ", num1/num2)

#Función para realizar una multiplicación de dos números
def division(num1, num2):
    print("El resultado es: ", num1*num2)

#Función para calcular la raiz cuadrada de un número
def raiz(num1):
    print("El resultado es: ", np.sqrt(num1))

#Función para calcular el exponente de un número
def exponente(num1):
    print("El resultado es: ", np.exp(num1))

#Función para calcular el seno de un número
def seno(num1):
    print("El resultado es: ", np.sin(num1))

#Función para calcular el coseno de un número
def coseno(num1):
    print("El resultado es: ", np.cos(num1))

#Función para calcular el tangente de un número
def tangente(num1):
    print("El resultado es: ", np.tan(num1))

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

if opc == 1:
    numeros()
    suma(num1,num2)
elif opc == 2:
    numeros()
    resta(num1,num2)
elif opc == 3:
    numeros()
    division(num1,num2)
elif opc == 4:
    numeros()
    multiplicacion(num1,num2)
elif opc == 5:
    numeros()
    raiz(num1)
elif opc == 6:
    numeros()
    exponente(num1)
elif opc == 7:
    numeros()
    seno(num1,num2)
elif opc == 8:
    numeros()
    coseno(num1,num2)
elif opc == 9:
    numeros()
    tangente(num1,num2)
elif opc == 10:
    print("\n Adiós")
else:
    print("\n Opción inválida \n")
