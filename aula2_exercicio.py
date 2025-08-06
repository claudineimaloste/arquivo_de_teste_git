

# Solicita ao usuário o valor que deseja sacar



valor = int(input("Digite o valor que deseja sacar: R$ "))

print('Informe um numero valido')

# Calcula a quantidade de notas de R$50
notas_50 = valor // 50
valor = valor % 50

# Calcula a quantidade de notas de R$10
notas_10 = valor // 10
valor = valor % 10

# Calcula a quantidade de notas de R$5
notas_5 = valor // 5
valor = valor % 5

# O que sobrou são as notas de R$1
notas_1 = valor

# Exibe o resultado
print("Notas fornecidas:")
print(f"R$50: {notas_50}")
print(f"R$10: {notas_10}")
print(f"R$5: {notas_5}")
print(f"R$1: {notas_1}")

