class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target = len(nums) // 3
        set_nums = set(nums)
        return [i for i in set_nums if (nums.count(i) > target)]