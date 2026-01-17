import random

class SLLNode:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  

    def _hash(self, key):
        return key % self.size

    def insert(self, key):
        index = self._hash(key)
        new_node = SLLNode(key, self.table[index])
        self.table[index] = new_node

    def search(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return True
            current = current.next
        return False
    
    