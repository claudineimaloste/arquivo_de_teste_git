
'''#exercicio - 1


# Entrada de dados com validação
salario_bruto = float(input("Digite o salário bruto: R$ "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

# Verifica se os valores são válidos
if salario_bruto < 0 or horas_trabalhadas < 0:
    print("Erro: Os valores não podem ser negativos.")
else:
    # Cálculo de adicional (hora extra)
    if horas_trabalhadas > 160:
        horas_extras = horas_trabalhadas - 160
        valor_hora = salario_bruto / 160
        adicional = horas_extras * valor_hora * 1.5  # Hora + 50%
    else:
        adicional = 0

    # Soma o adicional ao salário bruto para aplicar descontos
    salario_com_adicional = salario_bruto + adicional

    # Cálculo dos descontos
    if salario_com_adicional < 800:
        imposto_renda = 0
        encargos = 0
    elif salario_com_adicional <= 1600:
        imposto_renda = salario_com_adicional * 0.08
        encargos = salario_com_adicional * 0.05
    else:
        imposto_renda = salario_com_adicional * 0.15
        encargos = salario_com_adicional * 0.07

    # Cálculo do salário líquido
    salario_liquido = salario_com_adicional - imposto_renda - encargos

    # Exibição dos resultados
    print("\nResumo do pagamento:")
    print(f"Salário bruto: R$ {salario_bruto:.2f}")
    print(f"Adicional por horas extras: R$ {adicional:.2f}")
    print(f"Imposto de renda: R$ {imposto_renda:.2f}")
    print(f"Encargos: R$ {encargos:.2f}")
    print(f"Salário líquido: R$ {salario_liquido:.2f}")
'''
"""

#exercicio - 2

# Entrada do saldo inicial

saldo = float(input("Digite o saldo inicial da conta: R$ "))

# Início do loop de operações
while True:
    print("\n--- MENU DE OPERAÇÕES ---")
    print("10 - Saque em dinheiro")
    print("33 - Depósito")
    print("4  - PIX")
    print("1  - Sair")
    
    codigo = int(input("Digite o código da operação desejada: "))

    # Encerrar o programa
    if codigo == 1:
        print("Encerrando operações. Obrigado!")
        break

    # Saque
    elif codigo == 10:
        saque = float(input("Digite o valor para saque: R$ "))
        if saque > saldo:
            print("Saldo insuficiente para saque.")
        elif saque < 0:
            print("Valor inválido.")
        else:
            saldo -= saque
            print(f"Saque realizado. Saldo atual: R$ {saldo:.2f}")

    # Depósito em dinheiro
    elif codigo == 33:
        deposito = float(input("Digite o valor para depósito: R$ "))
        if deposito < 0:
            print("Valor inválido.")
        else:
            saldo += deposito
            print(f"Depósito realizado. Saldo atual: R$ {saldo:.2f}")

    # Depósito PIX
    elif codigo == 4:
        deposito_pix = float(input("Digite o valor do Pix: R$ "))
        if deposito_pix < 0:
            print("Valor inválido.")
        else:
            saldo += deposito_pix
            print(f"Depósito com Pix realizado. Saldo atual: R$ {saldo:.2f}")

    # Códigos inválidos
    else:
        print("Código inválido. Tente novamente.")




"""





