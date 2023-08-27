class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        length = len(str(x))
        while length > 0:
            first_digit =  x // 10 ** (length - 1) % 10
            last_digit = x % 10
            print(first_digit, last_digit)
            if (first_digit != last_digit):
                return False
            length -= 2
            x //= 10
        return True