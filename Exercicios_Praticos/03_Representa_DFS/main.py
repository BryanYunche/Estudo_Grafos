from DFS import DFS

#Cria um objeto do tipo Grafo
grafo01 = DFS()

#Adiciona vertices
grafo01.set_vertices(['A', 'B','C', 'D', 'E','F', 'G', 'H','I'])
grafo01.set_arestas([('A', 'B'), ('F', 'G'), ('H', 'F'), ('D', 'H'), ('C', 'D'), ('A', 'C'), ('F', 'I'), ('H', 'I')])

grafo01.DFS_constroi_dicionario()
for dicionario in range(len(grafo01.get_dicionario_grafos())):
    print(grafo01.get_dicionario_grafos()[dicionario])

print('=====================================================')
grafo01.DFS_procura()
for dicionario in range(len(grafo01.get_dicionario_grafos())):
    print(grafo01.get_dicionario_grafos()[dicionario])

print('=====================================================')
print(f'Ciclos do grafo: {grafo01.ciclos}')
print(f'Número de Arvores: {grafo01.arvores}')
