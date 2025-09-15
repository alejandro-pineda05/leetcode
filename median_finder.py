'''
Version TLE

class MedianFinder:

    def __init__(self):
        self.arr = []
        
    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()
        

    def findMedian(self) -> float:
        if len(self.arr) % 2 != 0:
            return self.arr[len(self.arr)//2]
        else:
            return (self.arr[len(self.arr)//2] + self.arr[len(self.arr)//2 - 1]) / 2

'''

import heapq

class MedianFinder:

    def __init__(self):
        self.arr_left = [] # los mas pequeños (como quiero el mas grande de aqui y uso una cola de prioridad,
                           # son negativos (asi eligiendo el mas pequeño me quedo con el mas grande))

        self.arr_right = [] # los mas grandes
        
    def addNum(self, num: int) -> None:
        
        if self.arr_left == [] and self.arr_right == []: # Primera iteracion
            heapq.heappush(self.arr_left, -num)
        elif self.arr_right == []: # La de la izda solo tiene un elemento
            if num >= abs(self.arr_left[0]): # si es mayor o igual que el que hay en la de la izda, lo añado a la dcha
                heapq.heappush(self.arr_right, num)
            else: # si no, el que hay en la izda lo paso a la dcha y el nuevo num lo meto en la izda
                heapq.heappush(self.arr_right, -heapq.heappop(self.arr_left))
                heapq.heappush(self.arr_left, -num)
        
        elif self.arr_left == []: # La de la dcha solo tiene un elemento
            if num <= abs(self.arr_right[0]): # si el num es menor o igual que el que hay en la dcha, lo meto en la izda
                heapq.heappush(self.arr_left, -num)
            else: # si el numero es mayor que el de la dcha, paso el de la dcha a la izda y el nuevo num lo meto en la dcha
                heapq.heappush(self.arr_left, -heapq.heappop(self.arr_right))
                heapq.heappush(self.arr_right, num)

        else: # Ninguna de las dos listas está vacía
            if len(self.arr_left) == len(self.arr_right): # si las dos listas tienen el mismo tamaño,
                # tengo que dejar la lista de la izda con un elemento mas que la otra
                if num <= abs(self.arr_right[0]):
                    heapq.heappush(self.arr_left, -num)
                else:
                    heapq.heappush(self.arr_left, -heapq.heappop(self.arr_right))
                    heapq.heappush(self.arr_right, num)

            else: # si la lista de la izda tiene un elemento mas que la de la dcha,
                #tengo que hacer que ambas tengan el mismo numero de elementos
                if num >= abs(self.arr_left[0]):
                    heapq.heappush(self.arr_right, num)
                else:
                    heapq.heappush(self.arr_right, -heapq.heappop(self.arr_left))
                    heapq.heappush(self.arr_left, -num)     
        

    def findMedian(self) -> float:
        if len(self.arr_left) == len(self.arr_right):
            return (- self.arr_left[0] + self.arr_right[0]) / 2
            
        else:    
            return - self.arr_left[0]

