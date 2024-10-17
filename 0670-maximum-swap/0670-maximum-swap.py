class Solution:
    def maximumSwap(self, num: int) -> int:
        num = [int(i) for i in str(num)]
        n = len(num)
        for i in range(n-1):
            index = i
            max_diff = 0
            for j in range(i+1, n):
                diff = num[j] - num[i]
                if diff != 0 and diff >= max_diff:
                    max_diff = diff
                    index = j
            if index != i:
                num[i], num[index] = num[index], num[i]
                break
        res = 0
        for i in range(n):
            res *= 10
            res += num[i]
        return res