class Solution:
    def reverse(self, x: int) -> int:
        if (x < 0):
            x = abs(x)
            negative = True
        else:
            negative = False

        reversedx = 0
        while (x != 0):
            digit = x % 10
            x //= 10

            if reversedx > (2**31 - 1) // 10 or (reversedx == (2**31 - 1) // 10 and digit > 7):
                return 0
            reversedx = reversedx * 10 + digit
        if (negative):
            return -1 * reversedx
        return reversedx