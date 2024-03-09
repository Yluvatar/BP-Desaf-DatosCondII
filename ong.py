import math


def factorial(numero):
    return math.factorial(numero)


def productoria(lista):
    return math.prod(lista)


def calcular(**kwargs):

    for key, value in kwargs.items():

        if key[:4] == 'fact':
            print(f"\nEl Factorial del número {value} es {factorial(value)}")
        elif key[:4] == 'prod':
            print(f"\nLa Productoría de {value} es {productoria(value)}")
        else:
            print(f"\nNo se reconoce la operación solicitada")

    exit()


print(calcular(fact_1=5, prod_1=[4, 6, 7, 4, 3], fact_2=6))
