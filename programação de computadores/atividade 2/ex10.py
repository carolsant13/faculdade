import math

a = float(input('digite o valor de a: '))
b = float(input('digite o valor de b: '))
c = float(input('digite o valor de c: '))

delta = b**2 - 4*a*c

if delta > 0:
    r1 = (-b + math.sqrt(delta)) / (2*a)
    r2 = (-b - math.sqrt(delta)) / (2*a)
    print(f'as raizes reais da equação são: {r1:.2f} e {r2:.2f}')
else:
    print('delta é negativo ou zero. Não sera possivel calcular raizes reais. ')