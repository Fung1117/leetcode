class TireNode:

    def __init__(self):
        self.childen = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TireNode()


    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            index = ord(char) - ord('a')
            if index not in current.childen:
                current.childen[index] = TireNode()
            current = current.childen[index]
        current.endOfWord = True

    def search(self, word: str) -> bool:
        stack = deque([self.root])
        for char in word:
            nextStack = deque()
            while stack:
                current = stack.pop()
                if char != '.':
                    index = ord(char) - ord('a')
                    if index in current.childen and current.childen[index]:
                        nextStack.append(current.childen[index])
                else:
                    for child in current.childen:
                        nextStack.append(current.childen[child])
            stack = nextStack
        return any(i.endOfWord for i in stack)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)