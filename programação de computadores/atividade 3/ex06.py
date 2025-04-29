positivos = 0 
negativos = 0
menor = 0

while True:
    valor = float(input('digite um numero real ou 0 para parar: '))

    if valor == 0:
        break

    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1

    if menor is None or valor < menor:
        menor=valor

    print(f'numeros positivos: {positivos}')
    print(f'numeros negativos: {negativos}')

    if menor is not None:
        print(f'o menor numero foi: {menor}')
    else:
        print('nenhum valor foi digitado.')