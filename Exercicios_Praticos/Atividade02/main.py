from Grafo_Matriz_Lista import Grafo


print("----------------- Grafo 01 -----------------")
grafo01 = Grafo()
grafo01.criaGrafo()


print("----------------- Grafo 02 -----------------")
grafo02 = Grafo(grafosTotais = ['A', 'B', 'C', 'D'], 
                arestasGrafo = [('A', 'B'), ('B', 'A'), ('B', 'C'), ('C', 'B'), ('C', 'A'), ('A', 'C'), ('D', 'B'), ('B', 'D')])

grafo02.apresentaMatrizAdj()


def produtoVetorialGrafo(grafoX, grafoY):
    #Produto dos vertices
    listaVertices01 = grafoX.getVertices()
    listaVertices02 = grafoY.getVertices()

    #produto Arestas
    listaArestas01 = grafoX.getArestas()
    listaArestas02 = grafoY.getArestas()

#Formato que está a lista de vertices: ['a', 'b', 'c', 'd']
#Formato que está a lista de arestas: [(a, b), (b, c), (c, a), (d, b)]

#Formato que está a lista de vertices: ['1', '2', '3', '4']
#Formato que está a lista de arestas: [('1', '2'), ('2', '3'), ('3', '1'), ('4', '2')]

#Lógica
#Multiplicar cada aresta do Grafo 01 por cada vertice do Grafo 02
    # Selecionar a aresta do Grafo 01 (x, y)
    # Multiplicar cada vertice do Grafo 02 , encontrado nas arestas, pela aresta (x, y) do Grafo 01
    # Sendo assim, cada vertice vai ocupar o a possição y no novo par ordenado gerado 
#Multiplicar cada aresta do Grafo 02 por cada vertice do Grafo 01
    # Selecionar a aresta do Grafo 02 (x, y)
    # Multiplicar cada vertice do Grafo 01 , encontrado nas arestas, pela aresta (x, y) do Grafo 02
    # Sendo assim, cada vertice vai ocupar o a possição x no novo par ordenado gerado
#Multiplicar cada vertice por cada vertice
    #Simplexmente vai ser V1 X V2

