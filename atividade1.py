print("=== Sistema de Cadastro  de Usuário e Senha ===")

usuarios = {}  # Dicionário: chave = matrícula, valor = senha
caracteres_especiais = "@#$%&*!"

# Cadastro
while True:
    usuario = input("Digite sua matrícula (mínimo 5 números): ")
    
    if not (usuario.isdigit() and len(usuario) == 11):
        print("Matrícula inválida. Digite no mínimo 11 números.")
        continue

    if usuario in usuarios:
        print("Essa matrícula já está cadastrada. Tente novamente.")
    else:
        break

# Validação de senha
while True:
    senha = input("Crie uma senha (mínimo 8 caracteres, com 1 letra maiúscula, 1 número e 1 caractere especial): ")

    if len(senha) >= 8 and \
       any(c.isupper() for c in senha) and \
       any(c.isdigit() for c in senha) and \
       any(c in caracteres_especiais for c in senha):
        usuarios[usuario] = senha  # Matrícula como chave
        print("\nCadastro realizado com sucesso!")
        break
    else:
        print("Senha inválida! A senha deve conter:")
        print("- Pelo menos 8 caracteres")
        print("- Pelo menos 1 letra maiúscula")
        print("- Pelo menos 1 número")
        print("- Pelo menos 1 caractere especial (@, #, $, etc.)")

# Login
print("\n=== Login ===")
login_matricula = input("Digite sua matrícula: ")
login_senha = input("Digite sua senha: ")

if login_matricula in usuarios and usuarios[login_matricula] == login_senha:
    print(f"\nLogin bem-sucedido! Bem-vindo(a), matrícula {login_matricula}!")
else:
    print("\nLogin falhou. Matrícula ou senha incorretos.")
