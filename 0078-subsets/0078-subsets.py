class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = [ [] ]
        for i in nums:
            tmp = []
            for j in power_set:
                tmp.append(j + [i])
            power_set = power_set + tmp
        return power_set