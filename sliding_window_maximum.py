from collections import deque

# Mi solucion al problema 239 de leetcode


def max_sliding_window(nums, k):
    if len(nums) <= 1 or k == 1:
        return nums
    
    res = []

    actual = deque()
    actual.append(nums[0])
    for i in range(1, len(nums)):
        if i >= k - 1 and nums[i - k + 1 - 1] == actual[0]:
            # si el que elimino de la ventana es el maximo actual, lo elimino tambien de la cola
            actual.popleft()

        if nums[i] > actual[0]:
            actual = deque()

        elif nums[i] > actual[-1]:
            while nums[i] > actual[-1]:
                actual.pop()

        actual.append(nums[i])

        if i >= k - 1:
            res.append(actual[0])
    
    return res



#print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))
print(max_sliding_window([9,10,9,-7,-4,-8,2,-6], 5))

# [9,10,9,-7,-4,-8,2,-6]








'''
# Chat gpt me ha recomendado hacerlo de esta otra forma donde la diferencia
# que tiene con la mia es que en la cola mete los indices de la lista, no los numeros de la lista

from collections import deque

def max_sliding_window(nums, k):
    dq = deque()  # guardará índices
    res = []

    for i, num in enumerate(nums):
        # 1. Sacar los índices que están fuera de la ventana
        if dq and dq[0] <= i - k:
            dq.popleft()

        # 2. Mantener la deque en orden decreciente
        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        # 3. Añadir el máximo actual a la respuesta
        if i >= k - 1:
            res.append(nums[dq[0]])

    return res



'''
