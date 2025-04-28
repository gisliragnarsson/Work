class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()
    
    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

    def peekFront(self):
        if (not self.isEmpty()):
            return self.items[self.size() - 1]
        
    def peekBack(self):
        if (not self.isEmpty()):
            return self.items[0]

queue = Queue()


print(queue.size()) # Prentast út 0


queue.enqueue(6)
queue.enqueue(3)
queue.enqueue(8)
queue.enqueue(7)


print(queue.peekBack()) # Prentast út 7


print(queue.dequeue()) # Prentast út 6


print(queue.size()) # Prentast út 3


queue.dequeue()
queue.dequeue()


print(queue.peekFront()) # Prentast út 7


print(queue.isEmpty()) # Prentast út False

