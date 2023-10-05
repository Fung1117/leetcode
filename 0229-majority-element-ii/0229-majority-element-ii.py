class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dir_nums = {}
        ary_nums = []
        target = len(nums) // 3
        for i in nums:
            if (i in ary_nums):
                continue
            if (i not in dir_nums):
                dir_nums[i] = 1
            else:
                dir_nums[i] += 1
            if (dir_nums[i] > target):
                ary_nums.append(i)
        return ary_nums