class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
            
        def helper(word, k):
            n = len(word)
            substringCount = 0
            vowels = {
                'a': 0,
                'e': 0,
                'i': 0,
                'o': 0,
                'u': 0,
            }
            consonants = 0
            lt_pt = rt_pt = 0
            while rt_pt < n:
                if word[rt_pt] in vowels:
                    vowels[ word[rt_pt] ] += 1
                else:
                    consonants += 1

                while all(vowels[vowel] > 0 for vowel in vowels) and consonants >= k:
                    substringCount += n - rt_pt
                    if word[lt_pt] in vowels:
                        vowels[ word[lt_pt] ] -= 1
                    else:
                        consonants -= 1
                    lt_pt += 1
                            
                rt_pt += 1

            return substringCount
        return helper(word, k) - helper(word, k + 1)