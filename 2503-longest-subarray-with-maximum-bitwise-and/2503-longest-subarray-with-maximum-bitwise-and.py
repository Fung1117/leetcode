class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        target = max(nums)
        count = 0
        current = 0
        for i in nums:
            if i == target:
                current += 1
            else:
                current = 0
            count = max(count, current)
        return count
