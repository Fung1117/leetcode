class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixArr1 = set()
        for value in arr1:
            while value > 0:
                if value in prefixArr1:
                    break
                prefixArr1.add(value)
                value //= 10
        maxCommonPrefix = 0
        for value in arr2:
            while value > 0 and len(str(value)) > maxCommonPrefix:
                if value in prefixArr1:
                    maxCommonPrefix = len(str(value))
                    break
                else:
                    value //= 10
        return maxCommonPrefix
