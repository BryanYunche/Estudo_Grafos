class Grafo():

    def __init__(self, vertices, arestas, matrizAdj, listaAdj):
        self.vertices = vertices
        self.arestas = arestas
        self.matrizAdj = matrizAdj
        self.listaAdj = listaAdj

    def getArestas(self):
        return self.arestas
    
    def setArestas(self, aresta):
        self.arestas += aresta
    
    def getVertices(self):
        return self.arestas
    
    def setVertices(self, vertices):
        self.arestas += vertices
    
    def matrizAdj(self, matriz):
        #Criar de maneira autômática identificadores pra linha e coluna de cada grafo
        pass
    
    def listaAdj(self, listaAdj):
        #
        pass
    
        