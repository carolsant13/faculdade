preco = float (input('digite o valor da compra : '))

if preco > 200:
    desc = preco * 0.20
    print(f'o valor final da compra com desconto de 20% fica {preco-desc:.2f}')
else:
    print(f'o valor da compra fica no total de {preco:.2f}')