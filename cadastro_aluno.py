import sqlite3

#menu principal do sistema 

def menu():
    print("n/ Sistema de Cadastro De Alunos")
    print("1. Cadastrar Aluno")
    print("2. Listar Alunos")
    print("3. Atualizar Aluno")
    pirnt("4. Excluir Aluno")
    print("5. Sair")

#cria o banco de dados e cria a tabela Aluno
def conectar():
    conexao = sqlite3.conect("Escola.db")
    cursor = conexao.cursor ()

    cursor.execute("""
             CREATE TABLE IF NOT EXISTS aluno(
                   id INTEGER PRIMARY KEY AUTOINCREMENT
                   nome TEXT NOT NULL,
                   email TEXT NOT NULL UNIQUE,
                   Idade INTEGER
                   )      
                   
                   
                   """ )


    conexao.commit()#garantir 
    conexao.close()#

    #funcao para cadastrar o aluno no DB
    def cadastrar_aluno(nome,email,idade):
    conexao = sqlite3.connect("escola.db")
    cursor = conexao.cursor ()

    try:
        cursor.execute("INSERT INTO aluno(nome,email,idade)VALUES (?,?,?)",
                       (nome,email,idade))
    except sqlite3.IntegrityError:
        print("email ja cadastrado")
    finally:
        conexao.close()

        if__name__=="__main__":