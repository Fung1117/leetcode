class MyHashMap:

    def __init__(self):
        self.hashmap = {}

    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value
        

    def get(self, key: int) -> int:
        if (key not in self.hashmap):
            return -1
        return self.hashmap[key]

    def remove(self, key: int) -> None:
        self.hashmap[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)