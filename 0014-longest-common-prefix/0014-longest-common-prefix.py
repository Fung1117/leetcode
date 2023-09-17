class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        longestString = strs[-1]
        shortestString = strs[0]
        answer = ""
        for i in range(min(len(longestString) ,len(shortestString))):
            if (longestString[i] != shortestString[i]):
                print(longestString[i], shortestString[i])
                return answer
            answer += shortestString[i]
        return answer
            