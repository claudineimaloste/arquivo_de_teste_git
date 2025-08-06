clientes = []

def cadastrar():
    while True:
        # Nome
        while True:
            nome = input("Nome: ").strip().upper()
            if len(nome) >= 3 and nome.replace(" ", "").isalpha():
                break
            else:
                print("Nome inválido. Deve ter ao menos 3 letras e conter apenas letras.")

        # CPF
        while True:
            cpf = input("CPF: ").strip().replace(".", "").replace("-", "").replace(" ", "")
            if len(cpf) == 11 and cpf.isdigit():
                break
            else:
                print("CPF inválido. Deve conter 11 dígitos.")

        # Telefone
        while True:
            telefone = input("Telefone: ").strip().replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
            if len(telefone) == 11 and telefone.isdigit():
                break
            else:
                print("Telefone inválido. Deve conter 11 dígitos.")

        # Email
        while True:
            email = input("Email: ").strip()
            if '@' in email and '.com' in email:
                break
            else:
                print("Email inválido.")

        # Criar dicionário do cliente
        cliente = {
            "nome": nome,
            "cpf": cpf,
            "telefone": telefone,
            "email": email
        }
        clientes.append(cliente)

        opcao = input("Deseja realizar outro cadastro? 1 - Sim | 2 - Não: ")
        if opcao != '1':
            break


def consultar():
    if not clientes:
        print("Não há informações cadastradas.")
    else:
        for i, cliente in enumerate(clientes):
            print(f"\nID: {i}")
            print(f"Nome: {cliente['nome']}")
            print(f"CPF: {cliente['cpf']}")
            print(f"Telefone: {cliente['telefone']}")
            print(f"Email: {cliente['email']}")


def excluir():
    try:
        codigo = int(input("Informe o ID do cliente a ser excluído: "))
        if 0 <= codigo < len(clientes):
            print(f"Confirma a exclusão do cliente {clientes[codigo]['nome']}?")
            confirmacao = input("Sim | Não: ").upper()
            if confirmacao == "SIM":
                del clientes[codigo]
                print("Cliente excluído com sucesso.")
            else:
                print("Exclusão cancelada.")
        else:
            print("Cliente não encontrado.")
    except ValueError:
        print("ID inválido. Digite um número.")


# Menu principal
while True:
    print("\n--- Menu ---")
    opcao = input("1 - Cadastrar\n2 - Consultar\n3 - Excluir\n4 - Sair\nOpção: ")

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
