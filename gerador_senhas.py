
import tkinter as tk
from tkinter import messagebox
import secrets
import string


# Função para gerar a senha
def gerar_senha():
    try:
        tamanho = int(campo_tamanho.get())

        if tamanho < 4 or tamanho > 128:
            messagebox.showwarning(
                "Atenção",
                "Escolha um tamanho entre 4 e 128 caracteres."
            )
            return

        caracteres = ""
        senha = []

        # Verifica os tipos de caracteres selecionados
        if var_maiusculas.get():
            grupo = string.ascii_uppercase
            caracteres += grupo
            senha.append(secrets.choice(grupo))

        if var_minusculas.get():
            grupo = string.ascii_lowercase
            caracteres += grupo
            senha.append(secrets.choice(grupo))

        if var_numeros.get():
            grupo = string.digits
            caracteres += grupo
            senha.append(secrets.choice(grupo))

        if var_simbolos.get():
            grupo = "!@#$%&*()-_=+?"
            caracteres += grupo
            senha.append(secrets.choice(grupo))

        if not caracteres:
            messagebox.showwarning(
                "Atenção",
                "Selecione pelo menos um tipo de caractere."
            )
            return

        # Completa a senha com caracteres aleatórios
        while len(senha) < tamanho:
            senha.append(secrets.choice(caracteres))

        # Embaralha os caracteres
        secrets.SystemRandom().shuffle(senha)

        resultado = "".join(senha)

        # Exibe a senha gerada
        campo_resultado.config(state="normal")
        campo_resultado.delete(0, tk.END)
        campo_resultado.insert(0, resultado)
        campo_resultado.config(state="readonly")

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite um tamanho válido."
        )


# Função para copiar a senha
def copiar_senha():
    senha = campo_resultado.get()

    if senha:
        janela.clipboard_clear()
        janela.clipboard_append(senha)
        messagebox.showinfo(
            "Sucesso",
            "Senha copiada para a área de transferência!"
        )
    else:
        messagebox.showwarning(
            "Atenção",
            "Gere uma senha primeiro."
        )


# Configuração da janela principal
janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("420x510")
janela.resizable(False, False)
janela.configure(bg="#20232A")


# Título
titulo = tk.Label(
    janela,
    text="GERADOR DE SENHAS",
    font=("Arial", 20, "bold"),
    bg="#20232A",
    fg="white"
)
titulo.pack(pady=(25, 5))


subtitulo = tk.Label(
    janela,
    text="Crie senhas aleatórias e seguras",
    font=("Arial", 10),
    bg="#20232A",
    fg="#B0B0B0"
)
subtitulo.pack(pady=(0, 20))


# Área de configurações
frame = tk.Frame(janela, bg="#2D323C", padx=20, pady=15)
frame.pack(padx=25, fill="x")


# Tamanho da senha
tk.Label(
    frame,
    text="Tamanho da senha:",
    font=("Arial", 11, "bold"),
    bg="#2D323C",
    fg="white"
).pack(anchor="w")

campo_tamanho = tk.Entry(
    frame,
    font=("Arial", 12),
    justify="center",
    width=10
)
campo_tamanho.insert(0, "16")
campo_tamanho.pack(anchor="w", pady=8)


# Variáveis das opções
var_maiusculas = tk.BooleanVar(value=True)
var_minusculas = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_simbolos = tk.BooleanVar(value=True)


# Opções de caracteres
tk.Label(
    frame,
    text="Tipos de caracteres:",
    font=("Arial", 11, "bold"),
    bg="#2D323C",
    fg="white"
).pack(anchor="w", pady=(10, 5))


opcoes = [
    ("Letras maiúsculas (A-Z)", var_maiusculas),
    ("Letras minúsculas (a-z)", var_minusculas),
    ("Números (0-9)", var_numeros),
    ("Símbolos (!@#$%)", var_simbolos)
]

for texto, variavel in opcoes:
    tk.Checkbutton(
        frame,
        text=texto,
        variable=variavel,
        font=("Arial", 10),
        bg="#2D323C",
        fg="white",
        selectcolor="#20232A",
        activebackground="#2D323C",
        activeforeground="white"
    ).pack(anchor="w", pady=2)


# Botão para gerar senha
botao_gerar = tk.Button(
    janela,
    text="GERAR SENHA",
    font=("Arial", 11, "bold"),
    bg="#6C45D9",
    fg="white",
    activebackground="#5433B5",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=gerar_senha
)
botao_gerar.pack(fill="x", padx=45, pady=(20, 15), ipady=9)


# Campo de resultado
tk.Label(
    janela,
    text="Sua senha:",
    font=("Arial", 11, "bold"),
    bg="#20232A",
    fg="white"
).pack(pady=(0, 8))


campo_resultado = tk.Entry(
    janela,
    font=("Consolas", 12),
    justify="center",
    state="readonly",
    readonlybackground="#2D323C",
    fg="#65E6A5",
    relief="flat"
)
campo_resultado.pack(fill="x", padx=35, ipady=10)


# Botão para copiar
botao_copiar = tk.Button(
    janela,
    text="COPIAR SENHA",
    font=("Arial", 10, "bold"),
    bg="#343A46",
    fg="white",
    activebackground="#454D5B",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=copiar_senha
)
botao_copiar.pack(fill="x", padx=45, pady=15, ipady=8)


# Rodapé
tk.Label(
    janela,
    text="Gerador de senhas desenvolvido em Python",
    font=("Arial", 8),
    bg="#20232A",
    fg="#888888"
).pack(side="bottom", pady=12)


# Inicia a aplicação
janela.mainloop()
