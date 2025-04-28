import math

x1 = float(input('digite as coordenadas x do ponto 1: '))
y1 = float(input('digite as coordenadas y do ponto 1: '))
x2 = float(input('digite as coordenadas x do ponto 2: '))
y2 = float(input('digite as coordenadas y do ponto 2: '))

d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f'a distancia entre os pontos é {d:.2f}')