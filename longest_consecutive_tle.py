import heapq

# Problema 128 de leetcode


# Leetcode me lo acepta pero no es la mejor solucion
# Yo lo resolví en O(nlog(n)) cuando se requería hacerlo en O(n)

# Además no tiene mucho sentido hacer esto porque en realidad es casi lo mismo que hacer un sort.
# Y por tanto la complejidad es O(nlog(n)) cuando en el enunciado pone que hay que hacerlo en O(n)






def longestConsecutive(nums):
    if nums == []:
        return 0
    
    nums = list(set(nums)) # Eliminar duplicados

    heapq.heapify(nums)

    res = 1 # Inicializo la variable resultado con el valor 1
    cuenta = 1 # Cuenta de numeros consecutivos empieza en el 1

    mas_pequeño_previo = heapq.heappop(nums)

    while len(nums) > 0 and res <= cuenta + len(nums):
        mas_pequeño_actual = heapq.heappop(nums)
        if mas_pequeño_actual == mas_pequeño_previo + 1: # Si dos numeros son consecutivos
            cuenta += 1
            res = max(res, cuenta)
        else: # Si no son consecutivos, establecemos cuenta a 1
            cuenta = 1
        mas_pequeño_previo = mas_pequeño_actual
    
    return res


print(longestConsecutive([100,4,200,1,3,2]))
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
