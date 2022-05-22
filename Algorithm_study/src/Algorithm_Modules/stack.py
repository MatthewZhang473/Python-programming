class Stack:
    def __init__(self):
        self.elements = []

    def push(self, data):
        self.elements.append(data)

    def pop(self):
        return self.elements.pop()

stack = Stack()


for i in range(10):
    stack.push(i)

stack.pop()

print(stack.elements)