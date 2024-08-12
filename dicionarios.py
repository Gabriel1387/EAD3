meu_dicionario = {
    1: "Python",
    2: "Java",
    3: "PHP"
}
print("Conteúdo do meu_dicionario:", meu_dicionario)
print("Tipo de dados de meu_dicionario:", type(meu_dicionario))

for chave, valor in meu_dicionario.items():
    print(f"Chave: {chave}, Valor: {valor}")

print("Tamanho de meu_dicionario:", len(meu_dicionario))

dicionario_frutas = dict({
    1: {"nome": "limão", "tipo": "ácida"},
    2: {"nome": "laranja", "tipo": "ácida"},
    3: {"nome": "manga", "tipo": "semiácida"},
    4: {"nome": "maçã", "tipo": "semiácida"},
    5: {"nome": "banana", "tipo": "doce"},
    6: {"nome": "mamão", "tipo": "doce"}
})
print("Conteúdo do dicionario_frutas:", dicionario_frutas)

fruta_1 = dicionario_frutas[1]
print(f"Chave 1 - Nome: {fruta_1['nome']}, Tipo: {fruta_1['tipo']}")

fruta_2 = dicionario_frutas[2]
print(f"Chave 2 - Nome: {fruta_2['nome']}, Tipo: {fruta_2['tipo']}")

print("Valores de todas as chaves 'nome' e 'tipo' em dicionario_frutas:")
for chave, fruta in dicionario_frutas.items():
    print(f"Chave {chave} - Nome: {fruta['nome']}, Tipo: {fruta['tipo']}")
