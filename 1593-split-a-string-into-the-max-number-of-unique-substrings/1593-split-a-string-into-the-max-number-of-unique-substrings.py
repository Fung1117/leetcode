class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        maxSplit = [0]
        n = len(s)
        def dfs(i, uniqueSet):
            if i >= n:

                maxSplit[0] = max(maxSplit[0], len(uniqueSet))
                return
            else:
                for k in range(i + 1, n + 1):
                    if s[i:k] not in uniqueSet:
                        uniqueSet.add(s[i:k])
                        dfs(k, uniqueSet)
                        uniqueSet.remove(s[i:k])
        dfs(0, set())
        return maxSplit[0]