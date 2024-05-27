class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        value = -1
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    value = max(value, j - i - 1)
        return value