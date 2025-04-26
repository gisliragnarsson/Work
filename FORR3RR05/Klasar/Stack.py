class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        if (not self.isEmpty()):
            return self.items[self.size() - 1]

    def isEmpty(self):
        return self.size() == 0
    
    def size(self):
        return len(self.items)


s = Stack()

print(s.size()) # Prentast út 0

s.push(6)
s.push(3)
s.push(8)

print(s.peek()) # Prentast út 8

print(s.pop()) # Prentast út 8

print(s.size()) # Prentast út 2

s.pop()
s.pop()

print(s.isEmpty()) # Prentast True
