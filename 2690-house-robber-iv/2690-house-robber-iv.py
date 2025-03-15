class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left, right = min(nums), max(nums)
        
        def canRobWithCapability(nums, capability, k):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= capability:
                    count += 1
                    i += 2  # Skip the next house since they are adjacent
                else:
                    i += 1  # Move to the next house
            return count >= k
        
        while left < right:
            mid = (left + right) // 2
            if canRobWithCapability(nums, mid, k):
                right = mid  # Try for a smaller capability
            else:
                left = mid + 1  # Increase capability
        return left