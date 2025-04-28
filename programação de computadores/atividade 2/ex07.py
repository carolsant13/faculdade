idade = int(input('digite a sua idade: '))

if idade < 16:
    print('não-eleitor')
elif 18 <= idade <= 65:
    print('eleitor obrigatório')
else:
    print('eleitor facultativo')