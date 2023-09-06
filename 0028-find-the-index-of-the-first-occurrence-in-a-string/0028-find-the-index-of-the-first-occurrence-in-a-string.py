class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if (needle not in haystack):
            return -1
        if (needle == haystack):
            return 0
        lengthofstr = len(needle)
        for i in range(len(haystack)-lengthofstr + 1):
            if (haystack[i : i+lengthofstr] == needle):
                return i