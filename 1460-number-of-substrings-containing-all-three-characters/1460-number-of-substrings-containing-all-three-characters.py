class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        counter = { 'a': 0, 'b': 0, 'c': 0 }
        n = len(s)
        lt_pt = rt_pt = 0
        while rt_pt < n:
            counter[s[rt_pt]] += 1
            while all(counter[char] > 0 for char in counter):
                counter[s[lt_pt]] -= 1
                lt_pt += 1
                count += n - rt_pt
            rt_pt += 1
        return count
