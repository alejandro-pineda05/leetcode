# La solucion definitiva. No solo usa el diccionario para no tener que recorrer una larga lista,
# sino que el arbol lo recorre a la vez de arriba abajo y de abajo arriba

from collections import defaultdict


# Aviso, esta solucion es mejor porque explora el bfs bidireccionalmente
# pero es muy liosa y no se hasta que punto es rentable hacer algo asi por encima de la otra que he hecho





def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0
    
    L = len(beginWord)
    
    # Construir diccionario de patrones
    patrones = defaultdict(list)
    for word in wordList:
        for i in range(L):
            patron = word[:i] + "*" + word[i+1:]
            patrones[patron].append(word)
    
    # BFS bidireccional usando sets
    return BidirectionalBFS(set([beginWord]), set([endWord]), patrones, 1, set([beginWord]), set([endWord]))

def BidirectionalBFS(front1, front2, patrones, level, visited1, visited2):
    if not front1:
        return 0  # No hay camino
    
    # Siempre expandimos el frente más pequeño
    if len(front1) > len(front2):
        return BidirectionalBFS(front2, front1, patrones, level, visited2, visited1)
    
    next_front = set()
    L = len(next(iter(front1)))  # longitud de las palabras
    
    for word in front1:
        for i in range(L):
            patron = word[:i] + "*" + word[i+1:]
            for vecino in patrones[patron]:
                if vecino in front2:
                    return level + 1  # se encuentran los frentes
                if vecino not in visited1:
                    visited1.add(vecino)
                    next_front.add(vecino)
            # Limpiamos vecinos para no procesarlos otra vez
            patrones[patron] = []
    
    return BidirectionalBFS(next_front, front2, patrones, level + 1, visited1, visited2)
