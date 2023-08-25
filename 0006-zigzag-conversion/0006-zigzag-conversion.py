class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows == 1):
            return s
        zigzag = [ "" for _ in range(numRows) ]
        y, count = 0, 0
        increasing = True
        while (count != len(s)):
            zigzag[y] += s[count] 
            if (increasing):
                y += 1
            else:
                y -= 1
            if (y == 0 or y == numRows-1):
                increasing = not(increasing)
            count += 1
        answer = ""
        for i in zigzag:
           answer += i
        return  answer