"""implementing a hash table"""

from typing import List
class HashTable:
    """Hash table"""
    def __init__(self, size: int = 53):
        self.keyMap:List = [None]*size
    
    def hash(self, key:str):
        """Hashes a string to a valid array index"""
        total: int = 0
        PRIME: int = 31
        for i in range(min(len(key), 101)):
            char: str = key[i]
            value: int = ord(char) - 96
            total = (total * PRIME + value) % len(self.keyMap) or 53
        return total
    
    def set(self, key: any, value: any):
        """adds a key-value pair to the hash table"""
        index: int = self.hash(key)
        if not self.keyMap[index]:
            self.keyMap[index] = []
        self.keyMap[index].append([key, value])
    
    def get(self, key):
        """retrieves an item from the table based on the key"""
        index: int = self.hash(key)
        # self.keyMap[index] is [[], []]
        if self.keyMap[index]:
            for i in range(0, len(self.keyMap[index])):
                if self.keyMap[index][i][0] == key:
                    return self.keyMap[index][i][1]
        return None

table: HashTable = HashTable()
table.set("ken", 24)
table.set("ken", 30)
table.set("hello", "GoodBye")
print(table.get("hello"))
# print(table.keyMap)