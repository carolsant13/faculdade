valorPrestacao = float(input('digite o valor da multa em atraso: '))
multa = float (input('digite o valor da multa: '))
qtdDias = float(input('digite a quantidade de dias em atraso: '))

prestacao = valorPrestacao+(valorPrestacao*(multa/100)*qtdDias)

print(f'o valor final da prestação em atraso é {prestacao}')