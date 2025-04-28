import math

n = float(input('digite o número de lados do polígono regular: '))
s = float(input('digite o comprimento de cado lado: '))

area = (n * s**2) / (4 *math.tan(math.pi / n))

print(f'area do polígono regular é {area:.2f}')