# La solucion que propuse primero, leetcode la aceptaba pero no es la mejor:





# Problema 127 de leetcode.


# Se resuelve con un bfs porque la busqueda en anchura es la que te permite encontrar el camino mas corto

def ladderLength(beginWord, endWord, wordList):
    return LadderLengthAux(set([beginWord]), endWord, set(wordList), 1, len(wordList))

def LadderLengthAux(actuales, endWord, candidatas, level, max_level):
    #print(f"actuales: {actuales}, endWord: {endWord}, candidatas: {candidatas}, level: {level}")
    if level > max_level:
        return 0
    hijos = set()
    for a in actuales:
        for w in candidatas:
            if es_hijo(a, w):
                if w == endWord:
                    return level + 1

                hijos.add(w)

    for h in hijos:
        if h in candidatas:
            candidatas.remove(h)
    
    return LadderLengthAux(hijos, endWord, candidatas, level + 1, max_level)

def es_hijo(w1, w2):
    diferencias = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            diferencias += 1
    
    if diferencias == 1:
        return True
    else:
        return False
