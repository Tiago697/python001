import sqlite3

# Conectar ou criar o banco de dados
conn = sqlite3.connect("escola.db")
cursor = conn.cursor()

# Criar tabela de alunos
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    curso TEXT NOT NULL
)
""")

# Criar tabela de professores
cursor.execute("""
CREATE TABLE IF NOT EXISTS professores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    disciplina TEXT NOT NULL
)
""")

# Função para cadastrar aluno
def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    curso = input("Digite o curso do aluno: ")
    cursor.execute("INSERT INTO alunos (nome, curso) VALUES (?, ?)", (nome, curso))
    conn.commit()
    print("Aluno cadastrado com sucesso.\n")

# Função para cadastrar professor
def cadastrar_professor():
    nome = input("Digite o nome do professor: ")
    disciplina = input("Digite a disciplina do professor: ")
    cursor.execute("INSERT INTO professores (nome, disciplina) VALUES (?, ?)", (nome, disciplina))
    conn.commit()
    print("Professor cadastrado com sucesso.\n")

# Função para exibir todos os alunos
def mostrar_alunos():
    print("\n=== Lista de Alunos ===")
    cursor.execute("SELECT * FROM alunos")
    for row in cursor.fetchall():
        print(f"ID: {row[0]} | Nome: {row[1]} | Curso: {row[2]}")

# Função para exibir todos os professores
def mostrar_professores():
    print("\n=== Lista de Professores ===")
    cursor.execute("SELECT * FROM professores")
    for row in cursor.fetchall():
        print(f"ID: {row[0]} | Nome: {row[1]} | Disciplina: {row[2]}")

# Menu principal
def menu():
    while True:
        print("\n1 - Cadastrar Aluno")
        print("2 - Cadastrar Professor")
        print("3 - Mostrar Alunos")
        print("4 - Mostrar Professores")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            cadastrar_professor()
        elif opcao == "3":
            mostrar_alunos()
        elif opcao == "4":
            mostrar_professores()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

    conn.close()
    print("Programa encerrado.")

# Iniciar o programa
menu()
