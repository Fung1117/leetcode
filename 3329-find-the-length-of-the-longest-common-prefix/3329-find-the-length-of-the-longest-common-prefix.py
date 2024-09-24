class TrieNode:
    def __init__(self):
        self.children =  [None for _ in range(10)]
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, value: int)->None:
        value = str(value)
        current = self.root
        for val in value:
            if current.children[int(val)] is None:
                current.children[int(val)] = TrieNode()
            current = current.children[int(val)]
    def findLongestPrefix(self, value: int)-> int:
        value = str(value)
        current = self.root
        count = 0
        for val in value:
            if current.children[int(val)] is None:
                return count
            current = current.children[int(val)]
            count += 1
        return count

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # make use of trie
        trie = Trie()
        for value in arr1:
            trie.insert(value)
        return max( trie.findLongestPrefix(value) for value in arr2)

