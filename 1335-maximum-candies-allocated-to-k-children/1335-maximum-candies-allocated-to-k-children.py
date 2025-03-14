class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 0
        right = max(candies)

        while left < right:
            middle = (left + right + 1) // 2

            count = sum( pile // middle for pile in candies )

            if count >= k:
                left = middle
            else:
                right = middle - 1

        return left

