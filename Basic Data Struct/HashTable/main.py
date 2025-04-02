# HashTable Using Seprate Chaining

class Node:
    def __init__(self, key, value):
        self.key = key 
        self.value = value
        self.next = None
    
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key):
        return hash(key) * self.capacity
    
    def insert(self, key, value):
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.size += 1
            
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
        new_node =  Node(key, value)
        new_node.next = self.table[index]
