class MyHashSet:

    def __init__(self):
        self.keyRange = 769
        self.bucketArray = [Bucket() for i in range(self.keyRange)]
        
    
    def _hash(self,key):
        return key%self.keyRange
    
    def add(self, key: int) -> None:
        bucketIndex = self._hash(key)
        if self.contains(key) == False:
            self.bucketArray[bucketIndex].insert(key)
        

    def remove(self, key: int) -> None:
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].delete(key)
        

    def contains(self, key: int) -> bool:
        bucketIndex = self._hash(key)
        return self.bucketArray[bucketIndex].exists(key)

class Node:
    
    def __init__(self,value,nextNode=None):
        self.val = value
        self.next = nextNode
        
class Bucket:
    def __init__(self):
        self.head = Node(0)
        
    def insert(self,newValue):
        if not self.exists(newValue):
            newNode = Node(newValue, self.head.next)
            self.head.next = newNode
            
    def exists(self,value):
        x = self.head.next
        while x is not None:
            if x.val == value:
                return True
            x = x.next
        return False

    def delete(self,value):
        x = self.head.next
        prev = self.head
        while x is not None:
            if x.val == value:
                prev.next = x.next
                return
            prev = x
            x = x.next

    


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

obj = MyHashSet()
obj.add(3)
obj.add(5)
print(obj.contains(4))