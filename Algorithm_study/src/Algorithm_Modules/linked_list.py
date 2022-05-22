

class Node:
    def __init__(self,data_val) -> None:
        self.data_val = data_val
        self.next_val = None
    
class linked_list:
    def _init_(self):
        self.head_val = None

    def traverse(self, array):
        the_pivot = self.head_val
        while the_pivot != None:
            array.append(the_pivot.data_val)
            the_pivot  = the_pivot.next_val

    def insert(self,New_Node):
        New_Node.next_val = self.head_val
        self.head_val = New_Node

    def search(self, value):
        x = self.head_val
        while x != None and x.data_val != value:
            x = x.next_val
        return x

list1 = linked_list()

p1 = Node("apple")
list1.head_val = p1
p2 = Node("beta")
p3 = Node("gamma")
p4 = Node("alpha")

p1.next_val = p2
p2.next_val = p3

traversing = []
list1.insert(p4)
list1.traverse(traversing)
print(traversing)

print(list1.search("betaa"))