class Node:
    def __init__(self, key, value, next = None, prev = None):
        # DLL
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = {} # store key : node
        
        # two dummy pointers left and right for LRU and MRU
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left # connect the two pointers
    
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
    
    def insertBack(self, node):
        prev, next = self.right.prev, self.right
        node.prev, node.next = prev, next
        prev.next = next.prev = node

    def get(self, key: int) -> int:
        if key in self.hm:
            node = self.hm[key]
            # Move this node to the back (MRU)
            self.remove(node)
            self.insertBack(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            # Update the existing node and move it to the back
            node = self.hm[key]
            node.value = value
            self.remove(node)
            self.insertBack(node)
        else:
            # inserting new node
            node = Node(key, value)
            self.hm[key] = node
            self.insertBack(node)
            
            if len(self.hm) > self.capacity:
                lru = self.left.next
                self.remove(lru)
                del self.hm[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)