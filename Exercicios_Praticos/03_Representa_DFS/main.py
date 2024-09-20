lista = [1, 2, 3, 4, 5]
arestas = [(1,3), (2,5), (4,3), (2,2), (4,5)]
numVertices = len(lista)
matrizAdj = [[0 for _ in range(numVertices)] for _ in range(numVertices)]

print(matrizAdj)

for verticeY in lista:
    for verticeX in lista:
        for aresta in arestas:
            x, y = aresta
            if (verticeX == x and verticeY == y):
                pass 
