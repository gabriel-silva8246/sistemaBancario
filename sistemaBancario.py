menu = """

1 - Depósito
2 - Saque
3 - Extrato
0 - Sair

"""

saldo_bancario = 0
extrato = ""
limite = 500.00
numero_saques = 0
limite_saques = 3

while True:
    print(menu)
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        deposito = float(input("Insira o valor que você deseja depositar: "))
        if deposito > 0:
            saldo_bancario += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
        else:
            print("A operação é inválida!")

    elif opcao == 2:
        saque = float(input("Insira o valor que você deseja sacar: "))
        excedeu_saldo = saque > saldo_bancario
        excedeu_limite = saque > limite
        excedeu_saques = numero_saques >= limite_saques
        if excedeu_saldo:
            print("O valor excedeu o valor disponível na conta")
        elif excedeu_limite:
            print("O valor de saque excedeu o limite de saque")
        elif excedeu_saques:
            print("O número de saques diários foi atingido")
        elif saque > 0:
            saldo_bancario -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1
        else:
            print("A operação é inválida!")

    elif opcao == 3:
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo_bancario:.2f}")

    elif opcao == 0:
        break

    else:
        print("Operação inválida, favor escolher uma operação válida.")
