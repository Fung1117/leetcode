class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        h = []
        for num in nums:
            heappush(h, -1 * num)
        total = 0
        for i in range(k):
            score = -1 * heappop(h)
            total += score
            heappush(h, -1 * ceil(score / 3))
        return total