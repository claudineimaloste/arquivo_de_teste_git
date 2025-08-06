import tkinter as tk
from tkinter import messagebox

usuarios = {}
caracteres_especiais = "@#$%&*!"

def validar_senha(senha):
    return (
        len(senha) >= 8 and
        any(c.isupper() for c in senha) and
        any(c.isdigit() for c in senha) and
        any(c in caracteres_especiais for c in senha)
    )

def confirmar_senha(matricula, senha, conf_senha):
    if senha != conf_senha:
        messagebox.showerror("Erro", "As senhas devem ser iguais.")
        return

    usuarios[matricula] = senha
    messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
    entry_matricula.delete(0, tk.END)
    entry_senha.delete(0, tk.END)
    entry_confirmar_senha.delete(0, tk.END)
    tela_cadastro.destroy()

def cadastrar():
    matricula = entry_matricula.get()
    senha = entry_senha.get()
    conf_senha = entry_confirmar_senha.get()

    if not (matricula.isdigit() and len(matricula) >= 5):
        messagebox.showerror("Erro", "Matrícula inválida. Mínimo 5 números.")
        return

    if matricula in usuarios:
        messagebox.showerror("Erro", "Matrícula já cadastrada.")
        return

    if not validar_senha(senha):
        messagebox.showerror(
            "Erro", 
            "Senha inválida!\nA senha deve conter:\n- Pelo menos 8 caracteres\n- 1 letra maiúscula\n- 1 número\n- 1 caractere especial (@#$%&*!)"
        )
        return

    confirmar_senha(matricula, senha, conf_senha)

def login():
    matricula = entry_login_matricula.get()
    senha = entry_login_senha.get()

    if matricula in usuarios and usuarios[matricula] == senha:
        messagebox.showinfo("Login", f"Login bem-sucedido! Bem-vindo(a), matrícula {matricula}")
    else:
        messagebox.showerror("Erro", "Login falhou. Matrícula ou senha incorretos.")

def chamar_tela_cadastro():
    global tela_cadastro, entry_matricula, entry_senha, entry_confirmar_senha
    tela_cadastro = tk.Toplevel()
    tela_cadastro.title("Cadastro de Usuário")

    tk.Label(tela_cadastro, text="Cadastro de Usuário", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Label(tela_cadastro, text="Matrícula:").pack()
    entry_matricula = tk.Entry(tela_cadastro)
    entry_matricula.pack()

    tk.Label(tela_cadastro, text="Senha:").pack()
    entry_senha = tk.Entry(tela_cadastro, show="*")
    entry_senha.pack()

    tk.Label(tela_cadastro, text="Confirmar Senha:").pack()
    entry_confirmar_senha = tk.Entry(tela_cadastro, show="*")
    entry_confirmar_senha.pack()

    tk.Button(tela_cadastro, text="Cadastrar", command=cadastrar).pack(pady=5)

# Janela Principal
janela = tk.Tk()
janela.title("Sistema de Cadastro e Login")

tk.Label(janela, text="Login", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(janela, text="Matrícula:").pack()
entry_login_matricula = tk.Entry(janela)
entry_login_matricula.pack()

tk.Label(janela, text="Senha:").pack()
entry_login_senha = tk.Entry(janela, show="*")
entry_login_senha.pack()

tk.Button(janela, text="Login", command=login).pack(pady=5)

tk.Label(janela, text="Não possui cadastro?").pack(pady=10)
tk.Button(janela, text="Cadastro", background="blue", command=chamar_tela_cadastro).pack(padx=10)

janela.mainloop()
