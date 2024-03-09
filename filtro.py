import sys


def lee_filtros():
    try:
        valorarg = int(sys.argv[1])
        rangoarg = 'mayor' if len(sys.argv) < 3 else sys.argv[2].lower()

    except IndexError:
        raise IndexError(f'\nSe debe ingresar al menos el parámetro de Valor que debe ser entero\n')

    except ValueError:
        raise ValueError(f'\nSe debe ingresar un valor entero, no {sys.argv[1]}\n')

    return valorarg, rangoarg


precios = {'Notebook': 700000,
           'Teclado': 25000,
           'Mouse': 12000,
           'Monitor': 250000,
           'Escritorio': 135000,
           'Tarjeta de Video': 1500000}

try:
    valor, rango = lee_filtros()
except (IndexError, ValueError) as e:
    print(e)
    exit()

if rango not in ['mayor', 'menor', 'igual']:
    print('\nLo sentimos, no es una operación válida ([mayor], menor o igual)\n')
    exit()

if rango == 'mayor':
    mayores = ','.join([k for k, v in precios.items() if valor < v])
    print(f'\nLos productos mayores al umbral son: {mayores}\n')
elif rango == 'igual':
    iguales = ','.join([k for k, v in precios.items() if valor == v])
    print(f'\nLos productos iguales al umbral son: {iguales}\n')
else:
    menores = ','.join([k for k, v in precios.items() if valor > v])
    print(f'\nLos productos menores al umbral son: {menores}\n')
