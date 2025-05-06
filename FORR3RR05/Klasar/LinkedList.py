class Node:
    def __init__(self, newValue):
        self.value = newValue
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        newNode = Node(value)

        if (self.head == None):
            self.head = newNode
            return
        
        current = self.head
        while(current.next != None):
            current = current.next
        
        current.next = newNode
    
    def display(self):
        current = self.head
        while(current != None):
            print(current.value)
            current = current.next




l = LinkedList()

l.append(5)
l.append(3)
l.append(7)
l.append(9)

l.display()
