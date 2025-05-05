idade_aluno = 22
nome_aluno = "Iago Gonçalves Costa"

def exibe_dados_aluno(param_nome_aluno: str = "Iago Gonçalves Costa", param_idade_aluno: int = 22, param_status_prova: bool = False, param_telefone: str = "49 9 40028922") -> str:
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