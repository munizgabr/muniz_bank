menu = '''

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=>'''
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    match opcao:
        case "1":
            valor = float(input('Informe o valor do depósito: '))
            if valor > 0:
                saldo += valor
                extrato += f'Depósito realizado no valor de R${valor:.2f}\n'
            else:
                print('Finalizado! Valor inválido.')
        
        case "2":
            saque = float(input('Informe o valor do saque: '))
            
            saldo_excedido = valor > saldo
            limite_excedido = valor > limite
            limite_saque = numero_saques > LIMITE_SAQUES

            if saldo_excedido:
                print('Finalizado! Sem saldo disponível')
            elif limite_excedido:
                print('Finalizado! Valor do limite de saque excedido. Tente novamente.')
            elif limite_saque:
                print('Finalizado! Limite máximo de saques diário excedido. Tente novamente amanhã.')
            elif saque > 0:
                saldo -= saque
                extrato += f'Saque realizado no valor de R${saque:.2f}\n'
            else:
                print('Finalizado! Valor inválido.')

        case "3":
            print("\n############## EXTRATO ##############")
            print("Extrato indisponível por falta de movimentacao" if not extrato else extrato)
            print(f"\nSaldo: R${saldo:.2f}")
            print("#####################################")
        
        case "0":
            break
        
                
