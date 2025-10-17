#CRIAÇÃO DO BANCO DE DADOS

import sqlite3
from fileinput import close

con = sqlite3.connect('cadastro.db')
cursor = con.cursor()

#CRIÇÃO DA TABELA DE ALUNOS
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuario
(id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT,
ra INTEGER,
curso TEXT )
''')

con.commit()
con.close()

#FUNÇÃO PARA REGISTRAR DADOS DO ALUNO
def cadastro_aluno(nome, ra, curso):
    con = sqlite3.connect('cadastro.db')
    cursor = con.cursor()
    cursor.execute('INSERT INTO alunos (nome, ra, curso) VALUES (?, ?, ?)', (nome, ra, curso))
    con.commit()
    con.close()

#MENU DO ADMINISTRADOR

#FUNÇÃO PARA MOSTRAR A LISTA DE ALUNOS
def listar_alunos(msg):
    con = sqlite3.connect('cadastro.db')
    cursor = con.cursor()

    cursor.execute('SELECT * FROM alunos')
    alunos = cursor.fetchall()

    if len(alunos) == 0:
        print('Nenhum aluno foi cadastrado.')
    else:
        print(msg)
        for aluno in alunos:
            print(f'ID: {aluno[0]} | nome: {aluno[1]} | RA: {aluno[2]} | curso: {aluno[3]}')
    con.close()

while True:
    print('\n-- SISTEMA ESCOLAR --\n')
    print('1. Cadastrar aluno')
    print('2. Cadastrar turma')
    print('3. Listar alunos')
    print('4. Listar turmas')
    print('5. Sair')

    opc = int(input('\nEscolha uma opção: '))

    match opc:
        case 1:
            nome = str(input('Aluno: '))
            ra = str(input('RA: '))
            curso = str(input('CURSO: '))
            cadastro_aluno (nome, ra, curso)

        case 3:
            listar_alunos('\n-- LISTA DE ALUNOS --\n')

        case 5:
            print('Sistema finalizado ')
            break

        case _:
            print('\nOPÇÃO INVÁLIDA! Tente novamente.\n')