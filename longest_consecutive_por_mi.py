# Esta solucion al problema si que la he hecho yo y es O(n) en tiempo

def longest_consecutive(nums):
    nums = set(nums)
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return 1
    
    elementos_procesados = set()

    res = 1
    cuenta = 1

    for n in nums:
        if n in elementos_procesados:
            continue
        n_tratado = n
        while n_tratado + 1 in nums:
            cuenta += 1
            res = max(res, cuenta)

            n_tratado = n_tratado + 1
            elementos_procesados.add(n_tratado)
        cuenta = 1
    return res
        



print(longest_consecutive([100,4,200,1,3,2]))
print(longest_consecutive([0,3,7,2,5,8,4,6,0,1]))