
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        def helper(num, i):
            if num == 0:
                return True

            if 3 ** i > num:
                return False
            else:
                return helper( num, i + 1) or helper( num-3**i, i + 1)
        
        return helper(n, 0)
        
