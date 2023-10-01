class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index = len(s) - 1
        while (s[index] == " "):
            index -= 1
        count = 0
        while (s[index] != " "):
            count += 1
            if (index == 0):
                return count
            print(index)
            index -= 1
            
        return count