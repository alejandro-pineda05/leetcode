# Problema 1 de leetcode

# La gracia está en recorrer la lista solo una vez

def twoSum(nums, target):
    dicc = {}
    for i in range(len(nums)):
        if target - nums[i] in dicc:
            return [dicc[target - nums[i]], i]
        else:
            dicc[nums[i]] = i
        



            
