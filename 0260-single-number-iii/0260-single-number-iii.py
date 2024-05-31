class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        numbers = {}
        for i in nums:
            if i in numbers:
                numbers[i] += 1
            else:
                numbers[i] = 0
        ans = []
        for i in numbers:
            if numbers[i] == 0:
                ans.append(i)
        return ans
