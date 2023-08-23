class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubstring = 0
        position = 0
        subString = []
        while (position < len(s)):
            if (s[position] in subString):
                subString = subString[subString.index(s[position]) + 1:]
            
            subString.append(s[position])

            position += 1

            if (len(subString) > longestSubstring):
                longestSubstring = len(subString)

        return longestSubstring

            