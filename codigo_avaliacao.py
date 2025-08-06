
usuarios = {}  # Armazena usuários e senhas
caracteres_especiais = "@#$%&*!"


def validar_senha(senha):
    return (
        len(senha) >= 8 and
        any(c.isupper() for c in senha) and
        any(c.isdigit() for c in senha) and
        any(c in caracteres_especiais for c in senha)
    )

def cadastrar():

    while True:
    
        matricula = input('Informe sua matricula: ')
        senha = input("Informe uma senha: ")
        
        if not (matricula.isdigit() and len(matricula) >= 5):
            print("Erro", "Matrícula inválida. Mínimo 5 números.")
            return

        if matricula in usuarios:
            print("Erro", "Matrícula já cadastrada.")
            return

        if not validar_senha(senha):
            print("Erro", "Senha inválida!\nA senha deve conter:\n- Pelo menos 8 caracteres\n- 1 letra maiúscula\n- 1 número\n- 1 caractere especial (@#$%&*!)")
            return
        else: 
            usuarios[matricula] = senha
            fazer_login()
            break
        

def login():

   while True: 
        matricula = input('Informe sua matricula: ')
        senha = input("Informe sua senha: ")

        if matricula in usuarios and usuarios[matricula] == senha:
            print("Login", f"Login bem-sucedido! Bem-vindo(a), matrícula {matricula}")
            break
        else:
            print("Erro", "Login falhou. Matrícula ou senha incorretos.")        
            while True:
                opcao = input('Não possui cadastro? digite 0 ou Digite qualquer tecla para continuar')
                if opcao == '0':
                    cadastrar()
                    break
                else:
                    login()
                    break


def fazer_login ():
    while True:
        opcao = input("O que deseja fazer?\n1 - Login\n2 - Cadastro\nOpcão: ")
        if opcao == '1':
            login()
            break
        if opcao == '2':
            cadastrar()
            break
        else:
            print("informe uma opcao válida")

fazer_login()