import time
from termcolor import colored

saldo = 0
limite_diario = 3
extrato = []

while True:

    # input("Seja bem vindo, aperte ENTER para continuar...")

    limite_valor = 500
    menu = colored("MENU", "magenta")   
    print(f"""       

====================== {menu} ======================
        
        
    1 - Depositar
    2 - Sacar
    3 - Extrato 
    4 - Sair      
        
        
================================================== 
""")

    operação = int(input("Selecione a operação desejada: "))

    if operação == 1:

        deposito = float(input("Digite o valor de deposito: "))
        
        if deposito <= 0:

            print("Valor de deposito invalido")

        else: 
            print("")
            texto =" DEPÓSITO FEITO COM SUCESSO! ".center(50, " ")
            saldo += deposito
            print(colored(texto, "green"))
            extrato.append(f"Deposito +R$ {deposito}")

    if operação == 2:
        print(colored("""
Lembre-se, o limite por saque é de R$ 500,00...
""", "cyan"))
        time.sleep(2)
        saque = float(input("Digite o valor de saque: "))
        if saque <=0:
            print("valor invalido")
        elif saque > limite_valor:
            print(colored ("""           NEGADO             
valor do saque excede o limite.""","red"))
        elif limite_diario == 0 and saque <= saldo :
            print(colored("""               NEGADO             
Você excedeu o limite de saques diarios.""", "red"))
            limite_diario = 3
        elif saque <= limite_valor and  saque <= saldo:
           limite_diario -= 1
           saldo -= saque
           print(colored("""           
                 SAQUE APROVADO             
                                        ""","green"))
           extrato.append(f"Saque -R$ {saque}")
        else:
            print(colored("Saldo Insuficiente", "red"))
        
       
    if operação == 3:
        if len(extrato) == 0:
            print("Não a transaçoes a serem exibidas.")
        for i in extrato:
            if i[:8] == "Deposito":
                print(colored (i, "green" ))
            if i[:5] == "Saque":
                print(colored (i, "red" ))
        print("\nSaldo atual:")
        if saldo == 0:
            print(colored(f"R$ {saldo}", "red"))
        else:
            print(colored(f"R$ {saldo}", "green"))        
    if operação == 4:
        print("Obrigado por utilizar nosso serviço.")
        break
   
   
   
   
   
   
   
   
    # else:
        # operação == 0       






    # elif operação == 2:

    #     valor_saque =  float(input("Digite o valor de saque: "))

    #     excedeu_saldo = valor_saque > saldo
        
    #     excedeu_limite_diario = limite_diario < 
    #     if saldo >= valor_saque and limite_diario >= 3:
    #         saldo -= valor_saque
    #         limite_diario -= 1
    #         limite_diario = 3
    #         print("O saque foi realizado com sucesso.")
      
    #     elif limite_diario == 0:
    #         print("Você atingiu seu limite diario de saques.")
    #     else:
    #         print("Saldo insuficiente.")
        

        



        