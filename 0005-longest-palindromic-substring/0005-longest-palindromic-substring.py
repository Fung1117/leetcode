class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = s[0]
        for i in range(len(s)):
            longest_string = str()
            position = [j for j in range(len(s)) if s[i] == s[j]]
            for j in position:
                tmp = s[i : j + 1]
                if (tmp == tmp[::-1]):
                    longest_string = tmp
            if (longest_string is not None and len(longest_string) > len(palindrome)):
                palindrome = longest_string
        return palindrome
