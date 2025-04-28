agua = float(input('digite o valor da conta de água: '))
luz = float(input('digite o valor da conta de luz: '))
telefone = float(input('digite o valor da conta de telefone: '))
sal = float(input('digite o valor do seu salario: '))

desp = agua+luz+telefone

if sal >= desp:
    print(f'o seu salario {sal:.2f} é suficiente para o pagamento das despesas no valor de {desp:.2f}')
else:
    print(f'o seu salario {sal:.2f} não é suficiente para o pagamento das despesas no valor de {desp:.2f}')

