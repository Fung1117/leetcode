class Solution:
    def longestPalindrome(self, s: str) -> str:

        longestString = s[0]

        for i in range(len(s)):
            subString = ""
            position = [j for j in range(i+1, len(s)) if s[j] == s[i]]
            if (len(position) == 0 or position[-1] - i < len(longestString) ):
                continue
            for j in position:
                tempString = s[i:j + 1]
                if (tempString != tempString[::-1]):
                    tempString = ""
                if (tempString != ""):
                    subString = tempString
            if (len(subString) > len(longestString)):
                longestString = subString 
        
        return longestString