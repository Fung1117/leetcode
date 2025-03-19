class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        for i in range(len(nums) - 2):
            if nums[i] == 1:
                continue
            for j in range(i, i + 3):
                nums[j] = (nums[j] + 1) % 2
            operations += 1
        if sum(nums) == len(nums):
            return operations
        return -1