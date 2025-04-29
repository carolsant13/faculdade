n = int(input("Digite a quantidade de termos da sequência de Fibonacci: "))

a, b = 1, 1

sequencia = []

for _ in range(n):
    sequencia.append(a)
    a, b = b, a + b

print("Sequência de Fibonacci:")
print(", ".join(str(num) for num in sequencia))
