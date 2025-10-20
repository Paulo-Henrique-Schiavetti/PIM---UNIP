# CRIAÇÃO DOS BANCOS DE DADOS

import sqlite3
from fileinput import close

# cria ou conecta ao banco de dados existente ---------------------------------------------------------------------------------

con = sqlite3.connect('banco.db')
cursor = con.cursor()

# definição de classes para facilitar a criação de dados para preencher as tabelas -------------------------------------------

# classe "Administrador"

class Administrador:
    login = ""
    senha = ""
    nome = ""

    def __init__(self, login, senha, nome):
        self.login = login
        self.senha = senha
        self.nome = nome

# classe "Aluno"

class Aluno:
    ra = ""
    senha = ""
    nome = ""
    turma = 0

    def __init__(self, ra, senha, nome, turma):
        self.ra = ra
        self.senha = senha
        self.nome = nome
        self.turma = turma

# classe "Turma"

class Turma:
    nome_curso = ""
    ano_inicio = 0

    def __init__(self, nome, ano):
        self.nome_curso = nome
        self.ano_inicio = ano

# Comando que eu uso para deletar os dados das tabelas para testes, True = deletar -------------------------------------------

if False:
    cursor.execute('DROP TABLE administrador')
    cursor.execute('DROP TABLE alunos')
    cursor.execute('DROP TABLE turmas')

# criação das tabelas no banco de dados --------------------------------------------------------------------------------------

# tabela "administrador"

cursor.execute('''
CREATE TABLE IF NOT EXISTS administrador
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT,
    senha TEXT,
    nome TEXT)
    ''')

# tabela "alunos" 

cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    ra TEXT,
    senha TEXT,                  
    nome TEXT,
    turma INTEGER)
    ''')

# tabela "turmas"

cursor.execute('''
CREATE TABLE IF NOT EXISTS turmas
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_curso TEXT,
    ano_inicio TEXT)
    ''')


# trecho que verifica se as tabelas já tem dados, para não preencher duas vezes --------------------------------------------

adm_vazia = (cursor.execute('SELECT * FROM administrador LIMIT 1').fetchone() == None)
alunos_vazia = (cursor.execute('SELECT * FROM alunos LIMIT 1').fetchone() == None)
turmas_vazia = (cursor.execute('SELECT * FROM turmas LIMIT 1').fetchone() == None)

# criação de administradores -----------------------------------------------------------------------------------------------

if adm_vazia:
    adms = list()

    adms.append(Administrador("adm123", "adm123", "ademir"))
    adms.append(Administrador("ADM9876", "password", "ademilson"))

    # inserção dos adms na tabela

    for adm in adms:
        cursor.execute('INSERT INTO administrador (login, senha, nome) VALUES (?, ?, ?)', (adm.login, adm.senha, adm.nome))


# criação de alunos de exemplo ---------------------------------------------------------------------------------------------

if alunos_vazia:
    alunos = list()

    alunos.append(Aluno("F3212J5", "senha123", "Alex da Silva", 1))
    alunos.append(Aluno("G5432I9", "senha321", "Beatriz da Silva", 1))
    alunos.append(Aluno("H2234U7", "azul123", "Carlos da Silva", 2))
    alunos.append(Aluno("D8732N3", "vermelho321", "Daniel da Silva", 2))
    alunos.append(Aluno("A4562R4", "verde123", "Eduardo da Silva", 3))
    alunos.append(Aluno("S4575F6", "amarelo567", "Flavia da Silva", 3))
    alunos.append(Aluno("R7890D1", "sardinha250g", "Gomes da Costa", 4))
    alunos.append(Aluno("H6675Q2", "ciano444", "Heribaldo da silva", 4))

    # inserção dos alunos na tabela

    for aluno in alunos:
        cursor.execute('INSERT INTO alunos (ra, senha, nome, turma) VALUES (?, ?, ?, ?)', (aluno.ra, aluno.senha, aluno.nome, aluno.turma))

# criação de turmas de exemplo --------------------------------------------------------------------------------------------

if turmas_vazia:
    turmas = list()

    turmas.append(Turma("Administração", 2025))
    turmas.append(Turma("Engenharia", 2025))
    turmas.append(Turma("Psicologia", 2025))
    turmas.append(Turma("Gastronomia", 2025))

    # inserção das turmas na tabela

    for turma in turmas:
        cursor.execute('INSERT INTO turmas (nome_curso, ano_inicio) VALUES (?, ?)', (turma.nome_curso, turma.ano_inicio))

# exibição dos alunos na tela ---------------------------------------------------------------------------------------------
print("--------------------------------------------------\n| \t\t Lista de alunos \t\t |\n--------------------------------------------------")

cursor.execute('SELECT * FROM alunos')
tabela = cursor.fetchall()

for aluno in tabela:
    print(f'ID: {aluno[0]} \t RA: {aluno[1]} \t senha: {aluno[2]} \t nome: {aluno[3]} \t\t ID da turma: {aluno[4]}')

# exibição das turmas e seus respectivos alunos na tela ------------------------------------------------------------------

print("--------------------------------------------------\n| \t\t Lista de turmas \t\t |\n--------------------------------------------------")


# puxando as turmas sem os alunos
cursor.execute('SELECT * FROM turmas')
tabela_turmas = cursor.fetchall()

# percorrendo as turmas e puxando os alunos de cada uma
for turma in tabela_turmas:
    print(f"\n| {turma[1]} - {turma[2]} |\n")

    # comando que puxa os alunos usando o id da turma (turma[0])
    tabela_alunos = cursor.execute('SELECT * FROM alunos WHERE turma=?', (turma[0],)).fetchall()

    # comando que exibe os alunos
    for aluno in tabela_alunos:
        print(f'ID: {aluno[0]} \t RA: {aluno[1]} \t senha: {aluno[2]} \t nome: {aluno[3]} \t\t turma: {turma[1]} - {turma[2]}')

# Fim do programa --------------------------------------------------------------------------------------------------------

con.commit()
con.close()