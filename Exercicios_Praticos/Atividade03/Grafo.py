class Grafo():

    def __init__(self, vertices, arestas, matrizAdj, listaAdj):
        self.vertices = vertices
        self.arestas = arestas
        self.matrizAdj = matrizAdj
        self.listaAdj = listaAdj

    def get_arestas(self):
        return self.arestas
    
    def set_arestas(self, aresta):
        self.arestas += aresta
    
    def get_vertices(self):
        return self.arestas
    
    def set_vertices(self, vertices):
        self.arestas += vertices

    def get_matriz_adj(self, matrizAdj):
        return self.matrizAdj
    
    def set_matriz_adj(self, matrizAdj):
        self.matrizAdj = matrizAdj

    def gera_matriz_adj(self, matriz):
        #Verifica antes se existe vertices
        #Gera matriz de adjacencias baseado nos vertices e nas arestas
        pass
    
    def imprime_matriz_adj(self, matriz):
        #Mostra um print da matriz
        pass

    def gera_lista_adj(self, listaAdj):
        #verifica se existe vertices
        #Gera lista de adjácencias baseado nos vertices e arestas
        pass
    
    #Função interna do grafo
    def consome_matriz(self, matriz):
        #Consome a matriz de rastreabilidade do grafo para gerar vertices e arestas
        #A matriz só tem 0 e 1
        pass

    #Função interna do grafo
    def consome_lista(self, lista):
        #Consome a lista de adjácencias e gera vertices e arestas
        pass

    
        