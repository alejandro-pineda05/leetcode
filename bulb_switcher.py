import math

class Solution:
    def bulbSwitch(self, n: int) -> int:
        # tengo que hacer n - multiplos de 3 que no sean pares
        if n == 0:
            return 0
        else:
            return  math.floor(math.sqrt(n))