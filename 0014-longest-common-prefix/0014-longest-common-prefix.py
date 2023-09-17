class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0]), 0, -1):
            prefix = strs[0][:i] 
            isPrefix = True
            for x in strs[1:]:
                if not(x.startswith(prefix)):
                    isPrefix = False
                    break
            if (isPrefix):
                return prefix
        return ""
