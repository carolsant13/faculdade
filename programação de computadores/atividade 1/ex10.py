import math

graus = float (input('digite o angulo em graus: '))

rad= math.radians(graus)

seno = math.sin(rad)
cosseno= math.cos(rad)
tangente= math.tan(rad)

print(f'seno: {seno:.4f}')
print(f'cosseno: {cosseno:.4f}')
print(f'tangente: {tangente:.4f}')