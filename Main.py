# PROGRAMA PRINCIPAL

import sqlite3
from fileinput import close

# CONECTA AO BANCO DE DADOS

con = sqlite3.connect('banco.db')
cursor = con.cursor()

# VARIAVEIS DO USUARIO

usuario = {'id': 0, 'is_adm': False, 'login': "", 'senha': "", 'nome': "", 'turma': "", 'nome_turma': "", 'ano_turma': 0}

aluno_selecionado = {'id': 0, 'ra': "", 'senha': "", 'nome': "", 'turma': 0, 'nome_turma': "", 'ano_turma': 0}
turma_selecionada = {'id': 0, 'nome_curso': "", 'ano_inicio': 0, 'alunos': ()}

# FUNÇÕES DE LOGIN

def login_aluno(ra, senha):
        aluno = cursor.execute('SELECT * FROM alunos WHERE ra=? AND senha=?', (ra, senha)).fetchone()
        if aluno != None:
            usuario['id'] = aluno[0]
            usuario['is_adm'] = False
            usuario['login'] = aluno[1]
            usuario['senha'] = aluno[2]
            usuario['nome'] = aluno[3]
            usuario['turma'] = aluno[4]
            if aluno[4]==0:
                usuario['nome_turma'] = "SEM TURMA"
                usuario['ano_turma'] = 0
            else:
                turma = cursor.execute('SELECT * FROM turmas WHERE id=?', (aluno[4],)).fetchone()
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
    cursor.execute('INSERT INTO alunos (ra, senha, nome, turma) VALUES (?, ?, ?, ?)', (ra, senha, nome, int(turma)))
    con.commit()
    return procurar_aluno(ra)

def cadastrar_turma(nome, ano):
    cursor.execute('INSERT INTO turmas (nome_curso, ano_inicio) VALUES (?, ?)', (nome, int(ano)))
    con.commit()
    return procurar_turma(cursor.execute('SELECT last_insert_rowid()').fetchone()[0])

def procurar_aluno(ra):
    aluno = cursor.execute('SELECT * FROM alunos WHERE ra=?', (ra,)).fetchone()
    if aluno != None:
        aluno_selecionado['id'] = aluno[0]
        aluno_selecionado['ra'] = aluno[1]
        aluno_selecionado['senha'] = aluno[2]
        aluno_selecionado['nome'] = aluno[3]
        aluno_selecionado['turma'] = aluno[4]
        if aluno[4]==0:
            aluno_selecionado['nome_turma'] = "SEM TURMA"
            aluno_selecionado['ano_turma'] = 0
        else:
            turma = cursor.execute('SELECT * FROM turmas WHERE id=?', (aluno[4],)).fetchone()
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
        alunos = cursor.execute('SELECT * FROM alunos WHERE turma=?', (id,)).fetchall()
        turma_selecionada['alunos'] = alunos
        return True
    else:
         return False
    
def listar_alunos():
    res = cursor.execute('SELECT * FROM alunos').fetchall()
    alunos = []
    for aluno in res:
        if aluno[4]==0:
            alunos.append(aluno+("SEM TURMA", 0))
        else:
            turma = cursor.execute('SELECT * FROM turmas WHERE id=?', (aluno[4],)).fetchone()
            alunos.append(aluno+(turma[1], turma[2]))
    return alunos

def listar_turmas():
    turmas = []
    res = cursor.execute('SELECT * FROM turmas').fetchall()
    for turma in res:
        alunos = cursor.execute('SELECT * FROM alunos WHERE turma=?', (turma[0],)).fetchall()
        turmas.append(turma+(alunos,))
        
    return turmas

def editar_aluno(ra, senha, nome, turma):
    id_turma = int(turma)
    cursor.execute('UPDATE alunos SET ra=?, senha=?, nome=?, turma=? WHERE id=?', (ra, senha, nome, id_turma, aluno_selecionado["id"]))
    con.commit()
    aluno_selecionado['ra'] = ra
    aluno_selecionado['senha'] = senha
    aluno_selecionado['nome'] = nome
    if id_turma != aluno_selecionado['turma']:
        aluno_selecionado['turma'] = id_turma
        if id_turma==0:
            aluno_selecionado['nome_turma'] = "SEM TURMA"
            aluno_selecionado['ano_turma'] = 0
        else:
            nova_turma = cursor.execute('SELECT * FROM turmas WHERE id=?', (id_turma,)).fetchone()
            aluno_selecionado['nome_turma'] = nova_turma[1]
            aluno_selecionado['ano_turma'] = nova_turma[2]
    return True
    
def excluir_aluno():
    cursor.execute('DELETE FROM alunos WHERE id=?', (aluno_selecionado["id"],))
    con.commit()
    aluno_selecionado['id'] = 0
    aluno_selecionado['ra'] = ""
    aluno_selecionado['senha'] = ""
    aluno_selecionado['nome'] = ""
    aluno_selecionado['turma'] = ""
    aluno_selecionado['nome_turma'] = ""
    aluno_selecionado['ano_turma'] = 0
    return True

def editar_turma(nome, ano):
    cursor.execute('UPDATE turmas SET nome_curso=?, ano_inicio=? WHERE id=?', (nome, ano, turma_selecionada["id"]))
    con.commit()
    turma_selecionada['nome_curso'] = nome
    turma_selecionada['ano_inicio'] = ano
    return True
    
def excluir_turma():
    con.commit()
    cursor.execute('DELETE FROM turmas WHERE id=?', (turma_selecionada["id"],))
    cursor.execute('UPDATE alunos SET turma=0 WHERE turma=?', (turma_selecionada["id"],))
    con.commit()
    turma_selecionada["id"] = 0
    turma_selecionada['nome_curso'] = ""
    turma_selecionada['ano_inicio'] = 0
    turma_selecionada['alunos'] = ()
    return True

        
def encerrar():
     con.commit()
     con.close()