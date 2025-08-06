


cadastro = {}
sulfixo_codigo = 2025
def cadastrar():
    while True:
        novo_cadastro = str(sulfixo_codigo) + str(len(cadastro) + 1)
        while True:
            nome = input("Nome: ").upper()            
            if len(nome) >= 3 and nome.replace(' ','').isalpha():
                break
            else:
                print("Nome inválido.Insira um nome válido")

        # CPF
        while True:
            cpf = input("CPF: ")
            cpf_numeros = cpf.replace('.', '').replace(' ', '').replace('-', '')
            if len(cpf_numeros) == 11:
                
                break
            else:
                print('CPF inválido.')

        # Telefone
        while True:
            telef = input("Telefone: ")
            telefone = telef.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
            if len(telefone) == 11:
                
                break
            else:
                print('Telefone inválido.')

        # Email
        while True:
            email = input("Email: ")
            if '@' in email and '.com' in email:
                
                break
            else:
                print('Email inválido.')
        # inserção dos dados.
        cadastro[novo_cadastro] = {'nome':nome,'cpf':cpf,'telefone':telefone,
                                  'email':email}
        # Continuar?
        opcao = input("Deseja realizar outro cadastro? 1 - Sim | 2 - Não: ")
        if opcao != '1':
            break


def consultar():
    if not cadastro:
        print('Não há informações cadastradas.')
    else:
        op = input('Que tipo de consulta deseja realizar: G - Geral | I - Individual ').upper()
        if op == 'G':
            for cod,dados in cadastro.items():
                print(f"\nMatricula: {cod} | "
                      f"Nome: {dados['nome']} | "
                      f"CPF: {dados['cpf']} | "
                      f"Telefone: {dados['telefone']} | "
                      f"Email: {dados['email']}\n")
        elif op == 'I':
            while True:                    
                    cod = input(f"informe o codigo do cliente: ")
                    
                    if cod not in cadastro:

                        print('Codigo invalido ou inexistente!')
                                              
                    else:
                        dados = cadastro.get(cod)
                        print(f"\nMatricula: {cod} | "
                            f"Nome: {dados['nome']} | "
                            f"CPF: {dados['cpf']} | "
                            f"Telefone: {dados['telefone']} | "
                            f"Email: {dados['email']}\n")
                        break
                    
        else:
            print("Opção Invalida")
            return      

def excluir():    
    try:
        codigo = input("Informe o código do Cliente (ID): ")
        if  not codigo in cadastro:
            print('Cliente não encontrado.')
        else:
            print(f"Confirma a exclusão do \nCliente {cadastro[codigo]['nome']} | "
                  f"CPF: {cadastro[codigo]['cpf']}?"
                  )
            opcao = input('Sim | Não: ').upper()
            if opcao == 'SIM':
                del cadastro[codigo]                
                print('Cliente excluído com sucesso.')
            else:
                print('Exclusão cancelada.')
    except ValueError:
         print('ID inválido. Por favor, digite um número válido.')


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
