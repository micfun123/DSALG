class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def peek(self):
        return self.items[0] if not self.is_empty() else None
    
    def length(self):
        return len(self.items)
    
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        
    def peek(self):
        return self.items[-1] if not self.is_empty() else None
    
    def length(self):
        return len(self.items)
    

#Convert Queue “12345” into Queue “54321”
def queue_reverse(queue):
    stack = Stack()
    while not queue.is_empty():
        stack.push(queue.dequeue())
    while not stack.is_empty():
        queue.enqueue(stack.pop())
    return queue

new_queue = Queue()
new_queue.enqueue(1)
new_queue.enqueue(2)
new_queue.enqueue(3)
new_queue.enqueue(4)
new_queue.enqueue(5)

reversed_new_queue = queue_reverse(new_queue)
while reversed_new_queue.is_empty() == False:
    print(new_queue.dequeue())