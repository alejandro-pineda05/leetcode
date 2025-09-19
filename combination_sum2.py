from typing import List

# Problema 40 de leetcode

# En este caso, a diferencia de la verison de Time Limit Exceed, estoy guardando en prev los casos que ya he explorado y me los salto

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        return combinationSum2Aux(candidates, target)

def combinationSum2Aux(candidates, target):
    candidates.sort()


    res = []

    def backtrack(start, path, target_restante):
        if target_restante == 0:
            res.append(path[:])
        
        elif target_restante < 0:
            return

        prev = None
        for i in range(start, len(candidates)):
            if prev == candidates[i]:
                continue

            path.append(candidates[i])
            backtrack(i + 1, path, target_restante - candidates[i])
            path.pop()

            prev = candidates[i]
    
    backtrack(0, [], target)
    return res












print(combinationSum2Aux([10,1,2,7,6,1,5],8))


print(combinationSum2Aux([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 39))