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

usuario = {'id': 0, 'is_adm': False, 'login': "", 'senha': "", 'nome': "", 'turma': "", 'nome_turma': "", 'ano_turma': 0}

aluno_selecionado = {'id': 0, 'ra': "", 'senha': "", 'nome': "", 'turma': 0, 'nome_turma': "", 'ano_turma': 0}
turma_selecionada = {'id': 0, 'nome_curso': "", 'ano_inicio': 0}


# FUNÇÕES DE LOGIN

def login_aluno(ra, senha):
        aluno = cursor.execute('SELECT * FROM alunos WHERE ra=? AND senha=?', (ra, senha)).fetchone()
        if aluno != None:
            turma = cursor.execute('SELECT * FROM turmas WHERE id=?', (aluno[4],)).fetchone()
            usuario['id'] = aluno[0]
            usuario['is_adm'] = False
            usuario['login'] = aluno[1]
            usuario['senha'] = aluno[2]
            usuario['nome'] = aluno[3]
            usuario['turma'] = aluno[4]
            usuario['nome_turma'] = turma[1]
            usuario['ano_turma'] = turma[2]
            return True
        else:
            return False

def login_adm(login, senha):
        admin = cursor.execute('SELECT * FROM administrador WHERE login=? AND senha=?', (login, senha)).fetchone()
        if admin != None:
            usuario['id'] = admin[0]
            usuario['is_adm'] = True
            usuario['login'] = admin[1]
            usuario['senha'] = admin[2]
            usuario['Nome'] = admin[3]
            return True
        else:
            return False
        
def cadastrar_aluno(ra, senha, nome, turma):
    cursor.execute('INSERT INTO alunos (ra, senha, nome, turma) VALUES (?, ?, ?, ?)', (ra, senha, nome, turma))
    con.commit()

def cadastrar_turma(nome, ano):
    cursor.execute('INSERT INTO turmas (nome_curso, ano_inicio) VALUES (?, ?)', (nome, ano))
    con.commit()

def procurar_aluno(ra):
    aluno = cursor.execute('SELECT * FROM alunos WHERE ra=?', (ra,)).fetchone()
    if aluno != None:
        turma = cursor.execute('SELECT * FROM turmas WHERE id=?', (aluno[4],)).fetchone()
        aluno_selecionado['id'] = aluno[0]
        aluno_selecionado['ra'] = aluno[1]
        aluno_selecionado['senha'] = aluno[2]
        aluno_selecionado['nome'] = aluno[3]
        aluno_selecionado['turma'] = aluno[4]
        aluno_selecionado['nome_turma'] = turma[1]
        aluno_selecionado['ano_turma'] = turma[2]
        return True
    else:
         return False

def procurar_turma(id):
    turma = cursor.execute('SELECT * FROM turmas WHERE id=?', (id,)).fetchone()
    if turma != None:
        turma_selecionada['id'] = turma[0]
        turma_selecionada['nome_curso'] = turma[1]
        turma_selecionada['ano_inicio'] = turma[2]
        return True
    else:
         return False
    
def listar_alunos():
     res = cursor.execute('SELECT * FROM alunos').fetchall()
     alunos = []
     for aluno in res:
          turma = cursor.execute('SELECT * FROM turmas WHERE id=?', (aluno[4],)).fetchone()
          alunos.append(aluno+(turma[1], turma[2]))
     return alunos

def listar_turmas():
     turmas = cursor.execute('SELECT * FROM turmas').fetchall()
     return turmas
        
def encerrar():
     con.commit()
     con.close()