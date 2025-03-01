class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ans = [ ]
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            if i + 1 < len(nums) and nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i + 1] = 0
            ans.append(nums[i])
        ans.extend([0] * (len(nums) - len(ans)))      
        return ans 