from Grafo_Matriz_Lista import Grafo

grafo01 = Grafo()
grafo02 = Grafo()

#Cadastra o Grafo
grafo01.cadastrarGrafos()
grafo02.cadastrarGrafos()

#Mostra as informações do Grafo 01
print("-----------------------------------------------------------------")
print(f'Vestices do Grafo1: {grafo01.getVertices()}')
print(f'Arestas do Grafo1: {grafo01.getArestas()}')

#Mostra as informações do Grafo 02
print("-----------------------------------------------------------------")
print(f'Vestices do Grafo2: {grafo02.getVertices()}')
print(f'Arestas do Grafo2: {grafo02.getArestas()}')

#Produto Cartesiano
vertices1 = grafo01.getVertices()
arestas1 = grafo01.getArestas()

vertices2 = grafo02.getVertices()
arestas2 = grafo02.getArestas()

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

