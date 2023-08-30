class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()  # Sort the input list in ascending order
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # Skip duplicate values of nums[i]
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1  # Skip duplicate values of nums[left]
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1  # Skip duplicate values of nums[right]
                    left += 1
                    right -= 1
        return answer