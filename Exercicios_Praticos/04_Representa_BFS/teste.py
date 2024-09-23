matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz_transposta =  [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

for linha in range(3):
    #Cria uma lista com as colunas
    for coluna in range(3):
        matriz_transposta[coluna][linha] = matriz[linha][coluna]

for i in range(3):
    print(matriz[i])

print(10*'=')
for i in range(3):
    print(matriz_transposta[i])
        

        