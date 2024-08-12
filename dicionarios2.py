dicionario_pessoas = {
    1: {'nome': 'Maria', 'idade': 26, 'nacionalidade': 'brasileira'}
}
print("Dicionário inicial:", dicionario_pessoas)

dicionario_pessoas.update({
    2: {'nome': 'João', 'idade': 30, 'nacionalidade': 'portuguesa'},
    3: {'nome': 'Ana', 'idade': 22, 'nacionalidade': 'espanhola'}
})
print("Dicionário atualizado:", dicionario_pessoas)

dicionario_copia = dicionario_pessoas.copy()
print("Cópia do dicionário:", dicionario_copia)

elemento_removido = dicionario_pessoas.pop(1)
print("Elemento removido:", elemento_removido)
print("Dicionário após remoção do elemento:", dicionario_pessoas)

ultimo_elemento = dicionario_pessoas.popitem()
print("Último elemento removido:", ultimo_elemento)
print("Dicionário após remoção do último elemento:", dicionario_pessoas)

dicionario_pessoas.clear()
dicionario_copia.clear()
print("Dicionário original após clear:", dicionario_pessoas)
print("Cópia do dicionário após clear:", dicionario_copia)

novo_dicionario = dict.fromkeys(['a', 'b', 'c'], 'valor_padrao')
print("Conteúdo do novo_dicionario:", novo_dicionario)
print("Itens do novo_dicionario:", novo_dicionario.items())
print("Chaves do novo_dicionario:", novo_dicionario.keys())
print("Valores do novo_dicionario:", novo_dicionario.values())
