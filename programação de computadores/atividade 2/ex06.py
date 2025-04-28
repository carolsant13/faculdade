turno = str(input('digite o seu turno de trabalho: n-notuno, m-matutino'))

qtd_horas = float(input('digite as horas trabalhadas: '))

if turno == 'n':
    sal= qtd_horas * 45
else: 
    sal= qtd_horas * 37.50

print (f'Você trabalha no turno {turno} e o seu salário é de {sal}')
