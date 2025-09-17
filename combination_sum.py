# Problema 39 de leetcode

def combinationSum(candidates, target):
    res = []

    def bactrack(i, target_acumulado, path):
        if target_acumulado == target:
            res.append(path[:])
            return
        
        elif target_acumulado >= target:
            return

        if i == len(candidates):
            return
        


        #En cada paso de la recursion, en una rama lo añado y me quedo en el mismo y en la otra paso al siguiente

        path.append(candidates[i])

        bactrack(i, target_acumulado + candidates[i], path)

        target_acumulado - path[-1]
        path.pop()

        bactrack(i + 1, target_acumulado, path)
    
    bactrack(0, 0, [])
    return res






















