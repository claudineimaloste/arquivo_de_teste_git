"""
Exemplo de uso de funções sem retorne e sem parametros
saldo = 0

def depositar():
    global saldo
    deposito = float(input("Digite o valor para depósito: R$ "))
    if deposito < 0:
        print("Valor inválido.")
    else:
        saldo += deposito
        print(f"Depósito realizado. Saldo atual: R$ {saldo:.2f}")

def sacar ():
    global saldo
    saque = float(input("Digite o valor para saque: R$ "))
    if saque > saldo:
        print("Saldo insuficiente para saque.")
    elif saque < 0:
        print("Valor inválido.")
    else:
        saldo -= saque
        print(f"Saque realizado. Saldo atual: R$ {saldo:.2f}")

def depositor_pix():
    global saldo
    deposito_pix = float(input("Digite o valor do Pix: R$ "))
    if deposito_pix < 0:
        print("Valor inválido.")
    else:
        saldo += deposito_pix
        print(f"Depósito com Pix realizado. Saldo atual: R$ {saldo:.2f}")

# Início do loop de operações
while True:
    print("\n--- MENU DE OPERAÇÕES ---")
    print("100 - Saque em dinheiro")
    print("101 - Depósito")
    print("102  - PIX")
    print("103 - Sair")
    
    codigo = input("Digite o código da operação desejada: ")

    # Encerrar o programa
    if codigo == '100':
        sacar()
    elif codigo == '101':
        depositar()
    elif codigo == '102':
        depositor_pix()
    elif codigo == '103':
        print("Encerrando operações. Obrigado!")
        break
    # Códigos inválidos
    else:
        print("Código inválido. Tente novamente.")

"""
"""
Função com retorno


"""

def somar (a,b):# estamos passando duas variaveis como parametro
    
    resultado = a + b # elas vão receber os valore informados fora da função

    return resultado


num = int(input('informe o um numero'))
num2 = int(input('informe outro numero: '))

soma = somar(num,num2) # para utilizar a função, podemos atribui-la a uma variavel
                       # e colocar como paramentros as variáveis que recebem os numeros
                       # 'num' vai passar o valor para 'a' e consequentemente,
                       # 'num2' vai passar o valor bara 'b'. O valor da soma, feita na fução
                       # é passado para vaiavel 'resultado' que retorna esse valor quando a 
                       #função é chamada.

print(f'A soma é: {soma}')
print(f'A soma é {somar(num,num2)}') #pode-se fazer dessa forma também, chamando a função
                                     # no print