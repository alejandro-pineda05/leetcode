# Problema 875 de leetcode

import math

def minEatingSpeed(piles, h):
    l, r = 1, max(piles)

    res = r

    if len(piles) == h:
        return res

    while l < r:
        mid_k = (l + r) // 2

        # si se lo puede comer me quedo con la izda y sino con la dcha
        horas_que_tarda = 0
        for monton in piles:
            horas_que_tarda += math.ceil(monton/mid_k)
            

        if horas_que_tarda > h:
            l = mid_k + 1

        else: # Puede ser una solucion, ahora hay que asegurarse
            res = min(res, mid_k)
            r = mid_k

    return res


#print(minEatingSpeed([3,6,7,11], 8))
#print(minEatingSpeed([30,11,23,4,20], 6))
print(minEatingSpeed([312884470], 312884469))

print(minEatingSpeed([1000000000,1000000000], 3))


