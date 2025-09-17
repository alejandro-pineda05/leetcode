def permute(nums):
    res = []

    def backtrack(path, used):
        if len(path) == len(nums):
            res.append(path[:])
            return
        # Probar todos los numeros que no hayamos usado en el path
        for i in range(len(nums)):
            if i in used:
                continue
            used.add(i)
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used.remove(i)
    
    backtrack([], set())

    return res

print(permute([0,1,2]))


