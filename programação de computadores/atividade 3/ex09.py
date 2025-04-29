n = int(input('digite um numero inteiro: '))
f = 1

for i in range (1, n):
    f *= i

print(f'o fatorial de {n} é {f}')