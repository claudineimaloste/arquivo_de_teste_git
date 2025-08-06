


lista_nome = []
lista_cpf = []
lista_telefone = []
lista_email = []

def cadastrar():
    while True:
        # Nome
        while True:
            nome = input("Nome: ").upper()            
            if len(nome) >= 3 and nome.replace(' ','').isalpha():
                lista_nome.append(nome)
                break
            else:
                print("Nome inválido.Insira um nome válido")

        # CPF
        while True:
            cpf = input("CPF: ")
            cpf_numeros = cpf.replace('.', '').replace(' ', '').replace('-', '')
            if len(cpf_numeros) == 11:
                lista_cpf.append(cpf_numeros)
                break
            else:
                print('CPF inválido.')

        # Telefone
        while True:
            telef = input("Telefone: ")
            telefone = telef.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
            if len(telefone) == 11:
                lista_telefone.append(telef)
                break
            else:
                print('Telefone inválido.')

        # Email
        while True:
            email = input("Email: ")
            if '@' in email and '.com' in email:
                lista_email.append(email)
                break
            else:
                print('Email inválido.')

        # Continuar?
        opcao = input("Deseja realizar outro cadastro? 1 - Sim | 2 - Não: ")
        if opcao != '1':
            break


def consultar():
    if not lista_nome:
        print('Não há informações cadastradas.')
    else:
        for i in range(len(lista_nome)):
            print(f"\nID: {i+1}")
            print(f"Nome: {lista_nome[i]}")
            print(f"CPF: {lista_cpf[i]}")
            print(f"Telefone: {lista_telefone[i]}")
            print(f"Email: {lista_email[i]}")


def excluir():
    #try:
        codigo = int(input("Informe o código do Cliente (ID): "))
        if codigo -1 < 0 or codigo -1 >= (len(lista_nome)):
            print('Cliente não encontrado.')
        else:
            print(f'Confirma a exclusão do cliente {lista_nome[codigo-1]}?')
            opcao = input('Sim | Não: ').upper()
            if opcao == 'SIM':
                del lista_nome[codigo-1]
                del lista_cpf[codigo-1]
                del lista_email[codigo-1]
                del lista_telefone[codigo-1]
                print('Cliente excluído com sucesso.')
            else:
                print('Exclusão cancelada.')
    #except ValueError:
        # print('ID inválido. Por favor, digite um número válido.')


# Menu principal
while True:
    print("\n--- Menu ---")
    opcao = input('1 - Cadastrar\n2 - Consultar\n3 - Excluir\n4 - Sair\nOpção: ')

    if opcao == '1':
        cadastrar()
    elif opcao == '2':
        consultar()
    elif opcao == '3':
        excluir()
    elif opcao == '4':
        print("Programa encerrado!")
        break
    else:
        print("Opção inválida. Tente novamente.")

        
    