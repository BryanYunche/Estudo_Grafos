from DFS import DFS

grafo01 = DFS()

#Adiciona vertices e arestas
matriz = [[0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0]]

grafo01.set_matriz_adj(matriz)
grafo01.imprime_matriz_adj()


"""print(grafo01.arestas)
grafo01.gera_lista_adj()
print(grafo01.get_lista_adj())
print(grafo01.get_vertices())

for vertice in grafo01.get_lista_adj():
    print(vertice)

grafo01.DFS_constroi_dicionario()"""



grafo01.DFS_procura()

for dicionario in range(len(grafo01.get_dicionario_grafos())):
    print(grafo01.get_dicionario_grafos()[dicionario])