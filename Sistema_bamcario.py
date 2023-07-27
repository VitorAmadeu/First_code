# First_code
Menu = '''  Operações:
[1]Saque
[2]Deposito
[3]Extrato
[4]sair \n\n'''
#variaveis
saldo = 0
limite_por_saque = 500
extrato = " "
numero_de_saque = 0
limite_de_Saques = 3

#codigo 

while (True):
    operacao_escolhida = int(input(Menu))
    
    if(operacao_escolhida == 1):
        if (numero_de_saque < limite_de_Saques):
            saque= float(input("qual o valor do saque:"))
            if(saque <= saldo):
                    saldo = saldo - saque
                    print(f"Saque no valor de R${saque:.2f}\n")
                    numero_de_saque += 1
                    extrato += f"Saque valor : R${saque}\n"
            else:
                print("Saldo insuficiente\n")
        else:
            print("Você não pode fazer mais saques\n")
            
    elif (operacao_escolhida == 2):
        deposito = float(input("Qual o valor deseja Depositar:\n"))
        if(deposito > 0):
            saldo = saldo + deposito
            print(f"Deposito no valor de R${deposito:.2f}\n")
            extrato += f"Deposito valor : R${deposito}\n" 
        else:
            print("Não é possivel depositar esse valor\n")
    
    elif (operacao_escolhida == 3):
        print(f"Saldo total:R${saldo}\n")   
        print(extrato)
    
    elif(operacao_escolhida == 4):
        break;
    
    else:
        print("A operação escolhida não existe.Escolha outra opção.\n")
