# PROGRAMA PRINCIPAL

import sqlite3
from fileinput import close

# ENFEITES TEMPORARIOS

texto1 = "-------------------------------------------\n | Sistema de cadastro de alunos e turmas |\n-------------------------------------------"
texto2 = "------------------\n| Login do aluno |\n------------------\n"
texto3 = "--------------------------\n| Login do administrador |--------------------------\n"

# CONECTA AO BANCO DE DADOS

con = sqlite3.connect('banco.db')
cursor = con.cursor()

# VARIAVEIS DO USUARIO

usuario_adm = False
id_usuario = 0
ra_usuario = ""
nome_usuario = ""


# FUNÇÕES DE LOGIN

def login_aluno():
    print(texto2)
    continuar = 3
    while continuar>0:
        ra = input("Digite o seu RA: ")
        senha = input("Digite a sua senha: ")
        aluno = cursor.execute('SELECT * FROM alunos WHERE ra=? AND senha=?', (ra, senha)).fetchone()
        if aluno != None:
            id_usuario = aluno[0]
            ra_usuario = aluno[1]
            nome_usuario = aluno[3]
            break
        print(f"Usuario ou senha incorretos, voce tem mais {continuar} chances. ")
        continuar -= 1
    print(f"\n\nSeja Bem-vindo {nome_usuario}!\n")

def login_adm():
    print(texto3)
    continuar = 3
    while continuar>0:
        login = input("Digite o seu login: ")
        senha = input("Digite a sua senha: ")
        aluno = cursor.execute('SELECT * FROM administrador WHERE login=? AND senha=?', (login, senha)).fetchone()
        if aluno != None:
            id_usuario = aluno[0]
            ra_usuario = aluno[1]
            nome_usuario = aluno[3]
            break
        print(f"Usuario ou senha incorretos, voce tem mais {continuar} chances. ")
        continuar -= 1
    print(f"\n\nSeja Bem-vindo {nome_usuario}!\n")

# PARTE INICIAL DO PROGRAMA

print(texto1)

print("Digite <1> para entrar como aluno. \nDigite <2> para entrar como administrador. \nDigite <0> para encerrar o programa.")
resposta = int(input("resposta: "))

while resposta !=0:
    if resposta == 1:
        login_aluno()
        break
    elif resposta == 2:
        login_adm()
        break
    else:
        print("Número inválido.")
        resposta = int(input("resposta: "))

print("Fim do programa.")