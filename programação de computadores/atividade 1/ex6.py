h = float(input('digite o valor da altura do tronco da pirâmide: '))
Bmenor = float (input('digite o valor da base menor: '))
Bmaior = float (input ('digite o valor da base maior'))

volume = h/3*(Bmaior**2 +Bmenor +(Bmaior**2 * Bmenor**2)**0.5)

print(f'o volume do tronco da piramide é {volume}')