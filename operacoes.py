def calcular_media(notas):
    if not notas:
        raise ValueError("A lista de notas não pode estar vazia.")
    return sum(notas) / len(notas)

def verificar_reprovacao(media):
    return media < 6

def gerar_relatorio_reprovados(dados_alunos, matriculas_reprovados):
    relatorio = []
    for matricula in matriculas_reprovados:
        aluno = dados_alunos.get(matricula)
        if aluno:
            nome = aluno['nome']
            media = aluno['media']
            relatorio.append(f'Aluno Reprovado: {nome} – Matrícula: {matricula} – Média Final: {media:.2f}')
    return relatorio

dados_alunos = {
    101: {'nome': 'Ana', 'media': calcular_media([5.5, 6.0, 6.5, 5.0])},
    102: {'nome': 'João', 'media': calcular_media([7.0, 7.5, 8.0, 7.5])},
    103: {'nome': 'Maria', 'media': calcular_media([4.5, 5.0, 5.5, 4.0])}
}

matriculas_reprovados = [matricula for matricula, dados in dados_alunos.items() if verificar_reprovacao(dados['media'])]
relatorio = gerar_relatorio_reprovados(dados_alunos, matriculas_reprovados)
for linha in relatorio:
    print(linha)
