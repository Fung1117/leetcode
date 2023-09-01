class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping.values():  # Opening bracket
                stack.append(char)
            elif char in mapping.keys():  # Closing bracket
                if not stack or stack.pop() != mapping[char]:
                    return False
        return not stack