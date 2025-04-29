soma = 0

for i in range(1, 11):
    n = float(input(f'digite o {i}° número: '))
    soma += n

media = soma / 10

print(f'soma dos números: {soma}')
print(f'a media dos números: {media}')