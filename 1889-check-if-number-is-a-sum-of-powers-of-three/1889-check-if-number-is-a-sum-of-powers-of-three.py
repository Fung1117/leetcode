import math

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        max_bound = int(math.log(n, 3)) + 2
        def helper(num, i):
            if num > n or i > max_bound:
                return False
            
            if num == n:
                return True
            else:
                return helper(num, i + 1) or helper(num + 3**i , i + 1)
        
        return helper(0, 0)
        
