import sqlite3

def mainMenu():
    print("\nSistema de Cadastro de Alunos")
    print("1. Cadastrar Aluno")
    print("2. Listar Alunos")
    print("3. Atualizar Aluno")
    print("4. Excluir Aluno")
    print("5. Sair")

def createTable():
    conexao = sqlite3.connect("escola.db")  
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS aluno (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            idade INTEGER
        )
    """)

    conexao.commit()
    conexao.close()

# Função para cadastrar aluno no banco de dados
def register(nome, email, idade):
    conexao = sqlite3.connect("escola.db")
    cursor = conexao.cursor()

    try:
        cursor.execute("INSERT INTO aluno (nome, email, idade) VALUES (?, ?, ?)",
                       (nome, email, idade))
        conexao.commit()
        print("Aluno cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: E-mail já cadastrado.")
    finally:
        conexao.close()

def display():
    conexao = sqlite3.connect("escola.db") #abri conexao com o Banco
    cursor = conexao.cursor()

    cursor.execute("SELECT*FROM aluno",)
    alunos = cursor.fetchall()
    
    
    conexao.close() #fecho conexao
    

    print ("lista de alunos cadastrados")
    for aluno in alunos:
        print(aluno)














# Bloco principal de execução
if __name__ == "__main__":
    createTable()
    while True:
        mainMenu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do aluno: ")
            email = input("Email do aluno: ")
            idade = int(input("Idade do aluno: "))
            register(nome, email, idade)
        elif opcao == "5":
            print("Saindo do sistema.")
            break
        else:
            print("Função ainda não implementada.")


