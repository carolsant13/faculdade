import random

def jogar_jokenpo():
    opcoes = ["pedra", "papel", "tesoura"]

    while True:
        jogador_vitorias = 0
        computador_vitorias = 0
        rodada = 1

        while jogador_vitorias < 3 and computador_vitorias < 3:
            print(f"\n-- Rodada {rodada} --")
            jogador = input("Escolha Pedra, Papel ou Tesoura: ").strip().lower()

            if jogador not in opcoes:
                print("Opção inválida. Tente novamente.")
                continue

            computador = random.choice(opcoes)

            print(f"Você escolheu: {jogador.capitalize()}")
            print(f"Computador escolheu: {computador.capitalize()}")

            if jogador == computador:
                print("Resultado: Empate!")
            elif (jogador == "pedra" and computador == "tesoura") or \
                 (jogador == "tesoura" and computador == "papel") or \
                 (jogador == "papel" and computador == "pedra"):
                print("Resultado: Você venceu!")
                jogador_vitorias += 1
            else:
                print("Resultado: Você perdeu!")
                computador_vitorias += 1

            print(f"Placar: Você {jogador_vitorias} x {computador_vitorias} Computador")
            rodada += 1


        if jogador_vitorias == 3:
            print("\nParabéns! Você ganhou a partida!")
        else:
            print("\nQue pena! O Computador ganhou a partida.")


        jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente != "s":
            print("Obrigado por jogar! Até a próxima!")
            break

if __name__ == "__main__":
    jogar_jokenpo()
