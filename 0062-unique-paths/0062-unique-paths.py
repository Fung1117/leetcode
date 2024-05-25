
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a = m + n - 2
        r = n - 1
        return math.comb(a, r)