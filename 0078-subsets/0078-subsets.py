class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = [ [] ]
        for i in nums:
            times = len(power_set)
            count = 0
            while count != times:
                power_set.append(power_set[count] + [i])
                count += 1
        return power_set