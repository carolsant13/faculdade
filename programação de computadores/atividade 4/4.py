def main():

    candidatos = {
        1: "José",
        2: "João",
        3: "Maria",
        4: "Ana"
    }


    votos_candidatos = {1: 0, 2: 0, 3: 0, 4: 0}
    votos_nulos = 0
    votos_branco = 0
    total_votos = 0

    print("Código dos votos:")
    for codigo, nome in candidatos.items():
        print(f"{codigo} - {nome}")
    print("5 - Voto Nulo")
    print("6 - Voto em Branco")
    print("Digite 0 para encerrar a votação.")

    while True:
        voto = int(input("Digite o código do voto: "))
        
        if voto == 0:
            break
        elif voto in votos_candidatos:
            votos_candidatos[voto] += 1
            total_votos += 1
        elif voto == 5:
            votos_nulos += 1
            total_votos += 1
        elif voto == 6:
            votos_branco += 1
            total_votos += 1
        else:
            print("Código inválido. Tente novamente.")

    # Mostra resultados
    print("\nResultado da votação:")
    for codigo, nome in candidatos.items():
        print(f"{nome}: {votos_candidatos[codigo]} voto(s)")

    print(f"Votos Nulos: {votos_nulos}")
    print(f"Votos em Branco: {votos_branco}")

    if total_votos > 0:
        percentual_nulos = (votos_nulos / total_votos) * 100
        percentual_branco = (votos_branco / total_votos) * 100

        print(f"Percentual de votos nulos: {percentual_nulos:.2f}%")
        print(f"Percentual de votos em branco: {percentual_branco:.2f}%")
    else:
        print("Nenhum voto foi computado.")

if __name__ == "__main__":
    main()
