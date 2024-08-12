lista_mesclada = [1, 2, 3, "Olá, Python", True, 12.6]
print("Conteúdo da lista_mesclada:", lista_mesclada)

lista_mesclada.append(["Lista aninhada"])
print("Conteúdo da lista_mesclada após append:", lista_mesclada)

lista_mesclada.insert(4, 5)
print("Conteúdo da lista_mesclada após insert:", lista_mesclada)
print("Tamanho atual da lista_mesclada:", len(lista_mesclada))

del lista_mesclada[1]
print("Conteúdo da lista_mesclada após remoção:", lista_mesclada)

nova_lista_mesclada = lista_mesclada[:5]
print("Conteúdo da nova_lista_mesclada:", nova_lista_mesclada)
