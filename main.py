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
