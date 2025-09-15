# Version de Chat gpt hecha para que se parezca a la mia pero que sea rapida,
# lo que hace es añadir un diccionario para que cada vez que busque los hijos
# de un nodo no busque en toda la lista de candidatas

# Hace lo mismo que he hecho yo solo que al inicio xon

from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        
        # Construir diccionario de patrones
        L = len(beginWord)
        patrones = defaultdict(list)
        for word in wordList:
            for i in range(L):
                patron = word[:i] + "*" + word[i+1:]
                patrones[patron].append(word)
        
        return LadderLengthAux(set([beginWord]), endWord, patrones, 1, len(wordList))

def LadderLengthAux(actuales, endWord, patrones, level, max_level):
    if level > max_level or not actuales:
        return 0
    
    hijos = set()
    for a in actuales:
        for i in range(len(a)):
            patron = a[:i] + "*" + a[i+1:]
            for w in patrones[patron]:
                if w == endWord:
                    return level + 1
                hijos.add(w)
            # Limpiamos los vecinos para no repetirlos en otros nodos
            patrones[patron] = []
    
    return LadderLengthAux(hijos, endWord, patrones, level + 1, max_level)




