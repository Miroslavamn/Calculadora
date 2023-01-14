# Calculadora - evaluación precurso
import numpy as np


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
    num1 = float(input("\n Ingresa el primer número: "))
    num2 = float(input("\n Ingresa el segundo número: "))
    resultado = num1 + num2
    print("\n El resultado es: ", resultado, "\n")
elif opc == 2:
    num1 = float(input("\n Ingresa el primer número: "))
    num2 = float(input("\n Ingresa el segundo número: "))
    resultado = num1 - num2
    print("\n El resultado es: ", resultado, "\n")
elif opc == 3:
    num1 = float(input("\n Ingresa el primer número: "))
    num2 = float(input("\n Ingresa el segundo número: "))
    resultado = num1 * num2
    print("\n El resultado es: ", resultado, "\n")
elif opc == 4:
    num1 = float(input("\n Ingresa el primer número: "))
    num2 = float(input("\n Ingresa el segundo número: "))
    resultado = num1 / num2
    print("\n El resultado es: ", resultado, "\n")
elif opc == 5:
    num1 = float(input("\n Ingresa un número: "))
    resultado = np.sqrt(num1)
    print("\n El resultado es: ", resultado, "\n")
elif opc == 6:
    num1 = float(input("\n Ingresa un número: "))
    resultado = np.np(num1)
    print("\n El resultado es: ", resultado, "\n")
elif opc == 7:
    num1 = float(input("\n Ingresa un número: "))
    resultado = np.sin(num1)
    print("\n El resultado es: ", resultado, "\n")
elif opc == 8:
    num1 = float(input("\n Ingresa un número: "))
    resultado = np.cos(num1)
    print("\n El resultado es: ", resultado, "\n")
elif opc == 9:
    num1 = float(input("Ingresa un número: "))
    resultado = np.tan(num1)
    print("\n El resultado es: ", resultado, "\n")
elif opc == 10:
    print("Adiós")
else:
    print("Opción invalida")
