class Queue:
    def __init__(self):
        self.items = []
        self.max_size = 15 

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        if len(self.items) < self.max_size:
            self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def peek(self):
        return self.items[0] if not self.is_empty() else None
    
    def length(self):
        return len(self.items)
    

new_queue = Queue()
new_queue.enqueue(1)
new_queue.enqueue(2)
new_queue.enqueue(3)
print(new_queue.peek())
print(new_queue.length())
print(new_queue.dequeue())
print(new_queue.length())
print(new_queue.peek())