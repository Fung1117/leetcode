class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubstring = 0
        for i in range(len(s)):
            count = 1
            substring = s[i]

            while (i + 1 < len(s) and s[i + 1] not in substring):
                i += 1
                substring += s[i]
                count += 1
            
            if (count > longestSubstring):
                longestSubstring = count
        return longestSubstring

            