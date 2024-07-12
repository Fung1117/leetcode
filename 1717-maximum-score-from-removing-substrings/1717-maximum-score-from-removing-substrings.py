class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stackA = []
        scoreA = 0
        stackB = []
        scoreB = 0
        for i in s:
            if len(stackA) > 0 and stackA[-1] == 'a' and i == 'b':
                stackA.pop()
                scoreA += x
            else:
                stackA.append(i)

            if len(stackB) > 0 and stackB[-1] == 'b' and i == 'a':
                stackB.pop()
                scoreB += y
            else:
                stackB.append(i)
        
        stackAB = []
        stackBA = []
        for i in stackA:
            if len(stackAB) > 0 and stackAB[-1] == 'b' and i == 'a':
                stackAB.pop()
                scoreA += y
            else:
                stackAB.append(i)
        for i in stackB:
            if len(stackBA) > 0 and stackBA[-1] == 'a' and i == 'b':
                stackBA.pop()
                scoreB += x
            else:
                stackBA.append(i)
        return max(scoreA, scoreB)

