class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        countS1 = Counter(s1.split())
        countS2 = Counter(s2.split())
        res = set()
        for word in countS1:
            if countS1[word] == 1 and word not in countS2:
                res.add(word)
        for word in countS2:
            if countS2[word] == 1 and word not in countS1 and word not in res:
                res.add(word)
        return list(res)