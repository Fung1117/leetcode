class Solution:
    def intToRoman(self, num: int) -> str:
        answer = ""
        i = 0
        while( num > 0 ):
            roman = num % 10
            num //= 10
            answer = self.toRoman(roman, i) + answer
            i += 2
        return answer
    
    def toRoman(self, num, pos):
        roman_book = ["I", "V", "X", "L", "C", "D", "M"]
        if (pos < len(roman_book)):
            i = roman_book[pos]
        if (pos + 1 < len(roman_book)): 
            j = roman_book[pos + 1]
        if (pos + 2 < len(roman_book)): 
            k = roman_book[pos + 2]
        #print(pos, i, j, k)
        match num:
            case 0:
                return ""
            case 1:
                return i
            case 2:
                return i * 2
            case 3:
                return i * 3
            case 4:
                return i + j
            case 5:
                return j
            case 6:
                return j + i
            case 7:
                return j + i * 2
            case 8:
                return j + i * 3
            case 9:
                return i + k