while True:
    nome = input('digite seu nome: ')
    if len(nome) >3:
        break
    print ('opção invalida')

while True:
        idade = int(input('digite sua idade: '))
        if 0 <= idade <= 150:
            break
        else:
            print('opção invalida')

while True:
        salario = int(input('digite seu salario: '))
        if salario > 0:
            break
        else:
            print('opção invalida')

while True:
        es = int(input('digite seu estado civil: '))
        if es in['s', 'c', 'v' 'd']:
            break
        else:
            print('opção invalida')

print ('informações')
print(f'nome: {nome}')
print(f'idade: {idade}')
print(f'salario: {salario}')
print(f'estado civil: {es}')
