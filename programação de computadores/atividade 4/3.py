while True:
    print("\nCALCULADORA:")
    print("1- somar")
    print("2- subtrair")
    print("3- multiplicar")
    print("4- dividir")
    print("0- sair")
    
    opcao = input("Insira sua opção: ")

    if opcao == "0":
        print("Até logo!...")
        break

    if opcao in ["1", "2", "3", "4"]:
        if opcao == "1":
            print("Opção - SOMAR")
        elif opcao == "2":
            print("Opção - SUBTRAIR")
        elif opcao == "3":
            print("Opção - MULTIPLICAR")
        elif opcao == "4":
            print("Opção - DIVIDIR")

        num1 = int(input("Insira o número desejado: "))
        num2 = int(input("Insira o próximo número: "))

        if opcao == "1":
            resultado = num1 + num2
        elif opcao == "2":
            resultado = num1 - num2
        elif opcao == "3":
            resultado = num1 * num2
        elif opcao == "4":
            if num2 != 0:
                resultado = num1 / num2
            else:
                print("Erro! Não é possível dividir por zero.")
                continue
        
        print(f"Resultado = {resultado}")
        print("\n(voltando para o menu....)")
    else:
        print("Opção inválida! Tente novamente.")
