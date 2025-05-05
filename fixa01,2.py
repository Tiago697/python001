#nao recebe e nao devolve nenhum retorno
def exibe_nome():
    print("nome")

#recebe parametro e nao devolve nenhum retorno
def exibe_nome(nome: str):
    print("nome")

#recebe o parametro nome que é do tipo string e 
#retorna um parametro tambem do tipo string
def exibe_nome(nome: str) -> str:
    print("nome")
    return "ok"

#esse tipo de funcao e uma funcao variadica que recebe uma lista de parametros
def mostra_numeros(*numeros) ->bool:
    print(numeros)
    for numero_atual in numeros[0]:
        print("o numero Atual lido foi", numero_atual)
    return True

'''tupla é uma sequência imutável de valores de qualquer tipo'''
#passa uma Tupla por parametro para a funcao mostra_numeros = tupla_numeros = (10,20,30,40,50,60,70,80,90,100)
tupla_numeros = (10,20,30,40,50,60,70,80,90,100)
print("numeros exibidos?", mostra_numeros(tupla_numeros))

#                0         1         2          3
lista_dados = ["teste", "debug", "compilar", "python"]

print("compilador"[0])

print(lista_dados[3][0])