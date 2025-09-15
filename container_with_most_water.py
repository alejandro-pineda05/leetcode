# Problema 11 leetcode



# este que parecia mas facil no he sido capaz de resolverlo solo.
# Tan solo era mover punteros que se inicializaban cada uno en un extremo,
# yo estaba intentando fuerza bruta optimizado a las alturas mas altas pero igualmente era fuerza bruta

def maxArea(height):
    left, right = 0, len(height) - 1
    res = 0
    
    while left < right:
        res = max(res, min(height[left], height[right]) * (right - left))
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return res

print(maxArea([1,8,6,2,5,4,8,3,7]))  # 49
