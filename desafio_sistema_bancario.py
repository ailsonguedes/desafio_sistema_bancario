saldo = 1500
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


menu = """

[d] Depositar
[w] Withdraw
[b] Balance
[e] Exit

=> """

def deposit(valD, saldo):
    saldo = saldo + valD
    return f'Valor depositado R${valD:.2f}\nValor atual R${saldo:.2f}\n'

def withdraw(valW, saldo):
    saldo = saldo - valW
    return f'Valor retirado R${valW:.2f}\nValor atual R${saldo:.2f}\n'

def balance(saldo):
    return f'Valor atual R${saldo:.2f}\n'

def menuF():
    print(f'MENU\n\n[d] Deposit\n[w] Withdraw\n[b] Balance\n[e] Exit\n')
    option = input('Select your option: ')

while True:  
               
    option = input(menu)
                
    if option == 'd':
        print('\n\nDeposit selected')
        val = float(input('Type your value: '))
            
        if val > 0:
            saldo += val
            print(f"Deposito: R$ {val:.2f}")
        else:
            print("Operação Inválida!")
            
    elif option == 'w':
        print('Withdraw selected')
        val = float(input('\n\nType your value: '))

        excedeu_saldo = val > saldo
        excedeu_limite = val > limite
        exedeu_saques = numero_saques > LIMITE_SAQUES
            
        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif excedeu_limite:
            print("Operação falhou! Limite insuficiente.")
        elif exedeu_saques:
            print("Operação falhou! Limite de saques diários excedidos.")
        elif val > 0:
            saldo -= val
            numero_saques += 1
            print(saldo)
                
    elif option == 'b':
        print('\n\nBalance selected')
        saldo = balance(saldo)
        print(saldo)
    elif option == 'e':
        print('\n\nExit selected')
        break 
    else:
        option = 'e'
        print("\n\nexit")
        break
        
    

