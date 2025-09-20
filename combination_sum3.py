# Problema 216 de leetcode

from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return combinationSum3Aux(k, n)
    
def combinationSum3Aux(k, n):
    res = []

    def backtrack(path, i, acum):
        if acum == n and len(path) == k:
            res.append(path[:])
            return
        elif i > 9 or len(path) > k or acum > n:
            return
        
        # Me quedo con el i actual y paso al siguiente
        path.append(i)
        backtrack(path, i + 1, acum + i)

        # O no selecciono el i actual y directamente paso al siguiente
        path.pop()
        backtrack(path, i+1, acum)

    backtrack([], 1, 0)
    return res


        


        

print(combinationSum3Aux(3, 9))
print(combinationSum3Aux(3, 9))




