from typing import List


# Version TLE del problema 40 de leetcode

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        return combinationSum2Aux(candidates, target)

def combinationSum2Aux(candidates, target):
    res = set()

    def backtrack(path, target_acumulado, i):

        if target_acumulado == target:
            res.append(tuple(sorted(path)))
            return
        
        if i == len(candidates) or target_acumulado > target:
            return

        # Puedo elegir añadir el actual o no añadirlo y pasar al siguiente

        backtrack(path + [candidates[i]], target_acumulado + candidates[i], i + 1)
        backtrack(path, target_acumulado, i + 1)

    backtrack([], 0, 0)

    return [list(r) for r in res]

