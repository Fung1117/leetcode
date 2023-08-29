class Solution:
    def romanToInt(self, s: str) -> int:
        romanBook = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        answer = 0
        i = 0
        while (i < len(s)):
            if (i + 1 != len(s) and romanBook[s[i]] < romanBook[s[i + 1]]):
                answer += romanBook[s[i + 1]] - romanBook[s[i]]
                i += 2
            else:
                answer += romanBook[s[i]]
                i += 1
        return answer