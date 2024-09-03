class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxLength = 0
        for i in nums:
            if i - 1 in nums:
                continue
            else:
                count = 1
                while i + 1 in nums:
                    i += 1
                    count += 1
                maxLength = max(maxLength, count)
        return maxLength
            
            




