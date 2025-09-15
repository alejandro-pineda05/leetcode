# Problema 200 de leetcode


def numIslands(matriz):
    # la matriz es una lista de listas
    islas_encontradas = 0

    matriz_inicial = []
    for fila in matriz:
        fila_matriz_inicial = []
        for el in fila:
            fila_matriz_inicial.append([el, False])
        matriz_inicial.append(fila_matriz_inicial)

    #printea_matriz(matriz_inicial)


    for i in range(len(matriz_inicial)):
        for j in range(len(matriz_inicial[0])):
            if matriz_inicial[i][j] == ["1", False]:
                islas_encontradas += 1
                explora(matriz_inicial, i, j)   

    return islas_encontradas 
    

    

def explora(matriz, i, j):
    matriz[i][j][1] = True

    #printea_matriz(matriz)

    hijos = []
    vecinos = [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]
    for v in vecinos:
        if v[0] >= 0 and v[0] < len(matriz) and v[1] >= 0 and v[1] < len(matriz[0]) and matriz[v[0]][v[1]][0] == "1" and matriz[v[0]][v[1]][1] == False:
            hijos.append(v)
    #print(f"hijos: {hijos}")

    for h in hijos:
        #print("entra")
        explora(matriz, h[0], h[1])

def printea_matriz(matriz):
    for fila in matriz:
        print(fila)
    print("\n")



print(numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))