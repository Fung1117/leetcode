class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        value = 0
        sign = 1
        if s.startswith('-'):
            sign = -1
            for i in s[1:]:
                if (i.isdigit()):
                    value *= 10
                    value += int(i)
                else:
                    break
        elif s.startswith('+'):
            for i in s[1:]:
                if (i.isdigit()):
                    value *= 10
                    value += int(i)
                else:
                    break
        else:
            for i in s:
                if (i.isdigit()):
                    value *= 10
                    value += int(i)
                else:
                    break
        fainalValue = sign * value
        if (fainalValue > 2147483647):
            return 2147483647
        elif (fainalValue < -2147483648):
            return -2147483648
        return fainalValue