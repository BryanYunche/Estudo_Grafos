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