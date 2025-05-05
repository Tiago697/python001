#Programação Procedural
#Variaveis
'''tipos de variaveis: primitivas
tipos: int -> para guardar numero inteiro'''

#padrão de projeto
#Tipar as variaveis
# snackcase = palavra_palavra. Ex: status_curso     
# camelCase = palavraPalavra. Ex: statusCurso      
'''idade_aluno: int = 10''' #pra saber desde o inicio que essa variavel vai guardar
'''nome_aluno: str = "Iago Costa"''' #str usado para palavras, texto
'''status_curso: bool = True''' #Falso ou verdadeiro
'''peso_aluno: float = 65,300''' #Float é usado para numeros com pontos flutuantes, com virgula

idade_aluno = 22
nome_aluno = "Iago Gonçalves Costa"

def exibe_dados_aluno(param_nome_aluno: str, param_idade_aluno: int, param_status_prova: bool, param_telefone: str) -> str:
    telefone: str = "49 9 40028922"
    status_prova: bool = False
    resposta: str = "OK!"
    if idade_aluno < 18: 
        return "erro_menor_idade"
    elif status_prova == False:
        return "erro002"

    print(f"a idade do aluno: {param_idade_aluno} é {param_idade_aluno} Anos e o fone de contato é: {param_telefone}")
    return resposta

resultado_funcao = exibe_dados_aluno("Iago Gonçalves Costa", 22, False, "49 9 40028922")

if resultado_funcao == "OK!": # se
    print(f"Sucesso!")
elif resultado_funcao == "erro_menor_idade": #elif -> senao se
    print(f"aluno é menor de idade, não pode ter habilitação")
elif resultado_funcao == "erro002":
    print("Aluno não atingiu a nota minima na prova")
else: #senao
    print(f"Ocorreu um erro!")



#OU USAR --> print(f"Depois de processar a funcao exibir_dados_aluno o resultado foi: {resultado_funcao}")


#outras estruturas -> complexas

#Orientação a Objeto
#Programação funcional