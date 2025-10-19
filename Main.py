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

def login_aluno(ra, senha):
        aluno = cursor.execute('SELECT * FROM alunos WHERE ra=? AND senha=?', (ra, senha)).fetchone()
        if aluno != None:
            usuario_adm = False
            id_usuario = aluno[0]
            ra_usuario = aluno[1]
            nome_usuario = aluno[3]
            return True
        else:
            return False

def login_adm(login, senha):
        usuario = cursor.execute('SELECT * FROM administrador WHERE login=? AND senha=?', (login, senha)).fetchone()
        if usuario != None:
            usuario_adm = True
            id_usuario = usuario[0]
            ra_usuario = usuario[1]
            nome_usuario = usuario[3]
            return True
        else:
            return False
        
def encerrar():
     con.commit()
     con.close()