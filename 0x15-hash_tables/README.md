# Hash Tables
Hash tables are data structures that store key value pairs.  
They are like arrays but keys are not ordered.  
They are very fast for adding, removing and getting values.  
They are inbuilt in most programming languages but it's a good idea to understand how they work.  

To implement hash table, we'll be using an array.  
In order to look up values by keys, we need a way to convert keys into valid indices.  
A function that performs this task is called a **hash function**.  
The idea is we pass a string to a hash function, and it gives you an index.  
The function should always give the same result for the same input, eg if we pass "orange" and it gives us 3, the next time we pass orange it should give us 3.

## What makes a good hash function
1. Fast (i.e Constant time).
1. Doesn't cluster outputs to specific indices, but distributes uniformly. for example, we don't want a hash function that is only spitting out 9 or 10 regardless of what we input.
1. Deterministic (same input yields the same output).

## writing our first hash function
There are many ways of building this hash function, this is not the "one solution to all algorithm".

```python
def hash(key:str, array_len: int):
    """Hashes a string to a valid array index"""
    total: int = 0
    PRIME: int = 31
    for i in range(min(len(key), 101)):
        char: str = key[i]
        value: int = ord(char) - 96
        total = (total * PRIME + value) % array_len
    return total
```

prime number has been used to distribute the output/reduce **collisions** (situations where 2 inputs yield the same output)

## Dealing with collisions
Two inputs may end up yielding the same output.  
There are 2 methods of dealing with collisions:  
- **Separate chaining** - at each index of our array, we store data using a more sophisticated data structure eg linked list or arrays.
- **Linear probing** - when we find a collision, we search through the array to find the next empty slot.

## A hash table class
```python
from typing import List
class HashTable:
    """Hash table"""
    def __init__(self, size: int = 53):
        self.keyMap:List = []*size
    
    def hash(self, key:str):
        """Hashes a string to a valid array index"""
        total: int = 0
        PRIME: int = 31
        for i in range(min(len(key), 101)):
            char: str = key[i]
            value: int = ord(char) - 96
            total = (total * PRIME + value) % len(self.keyMap)
        return total
```

### Set
1. Accepts a key and a value.
1. Hash the key
1. Store the key-value pair in the hash table via separate chaining.

```python
def set(self, key: any, value: any):
    """adds a key-value pair to the hash table"""
    index: int = self.hash(key)
    if not self.keyMap[index]:
        self.keyMap[index] = []
    self.keyMap[index].append([key, value])
```

### get
1. Accepts a key
1. Hashes the key.
1. Retrieves the key-value pair
1. If the key isn't found, return undefined.

```python
def get(self, key):
    """retrieves an item from the table based on the key"""
    index: int = self.hash(key)
    # self.keyMap[index] is [[], []]
    if self.keyMap[index]:
        for i in range(0, len(self.keyMap[index])):
            if self.keyMap[index][i][0] == key:
                return self.keyMap[index][i][1]
    return None
```

## Big O of hash tables
Insertion - O(1)  
Deletion - O(1)  
Access - O(1)  