class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counter = Counter(s1.split()) + Counter(s2.split())
        return [ word for word in counter if counter[word] == 1 ]