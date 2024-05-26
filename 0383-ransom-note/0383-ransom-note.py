class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        noteBook = {}
        for i in ransomNote:
            if i not in noteBook:
                noteBook[i] = 1
            else:
                noteBook[i] += 1
        for i in magazine:
            if i in noteBook:
                noteBook[i] -= 1
        for a, b in noteBook.items():
            if b > 0:
                return False
        return True