# Problema 347 de leetcode

'''

Este problema se resuelve utilizando una cola de prioridad.
La cola de prioridad a nivel practico es una lista cuyo primer elemento es el minimo,
resulta muy facil asi eliminar el elemento minimo de la lista sin recorrerla entera y
saber que en cada iteracion el elemento minimo siempre va a ser el primero.

No confundir con una lista ordenada de mayor a menor.

En este caso, la lista no esta ordenada, solo tenemos el elemento minimo en todo momento.
Detrás de la libreria importada, la cola de prioridad está implementada utilizando un arbol
binario cuya raiz siempre es el elemento mas pequeño.

Ese arbol se ha creado a partir de una lista de numeros (o elementos ordenables)
y se ha ido añadiendo como hijo el nodo mayor al que se pueda añadir que sea menor que el nodo actual

Es un algoritmo mas rapido que la ordenacion que solo nos aporta el elemento minimo en cada momento

'''


import heapq

def topKFrequent(nums, k):
    frecuencias = {}
    for n in nums:
        if n not in frecuencias:
            frecuencias[n] = 1
        else:
            frecuencias[n] += 1
    
    # Creo una cola de prioridad para saber en todo momento la frecuencia menor.
    # (  pero no me olvido que tengo que saber de que numero se trata,
    # por eso lo almaceno en tuplas: (frecuencia, numero)  )
    heap = []
    for f in frecuencias:
        heapq.heappush(heap,(frecuencias[f], f))
    
    while len(heap) > k:

        heapq.heappop(heap)

    return [x[1] for x in heap]





# Hago una pequeña modificacion para simplificar el codigo:
def topKFrequent2(nums, k):
    frecuencias = {}
    for n in nums:
        if n not in frecuencias:
            frecuencias[n] = 1
        else:
            frecuencias[n] += 1
    
    heap = []
    for f in frecuencias:
        heapq.heappush(heap,(frecuencias[f], f))
        if len(heap) > k:
            heapq.heappop(heap)


    return [num for frec, num in heap]



print(topKFrequent([1,2,4,5,6,7,3,2,1,4,6,3,2,4,5,2,3,1,2,13,3,6], 2)) # [3,2]
print(topKFrequent2([1,2,4,5,6,7,3,2,1,4,6,3,2,4,5,2,3,1,2,13,3,6], 2)) # [3,2]


