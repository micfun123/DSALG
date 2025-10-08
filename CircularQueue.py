
class CircularQueue:
    def __init__(self):
        self.items = []
        self.max_size = 15
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0
    def is_full(self):
        return self.size == self.max_size

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        self.rear = (self.rear + 1) % self.max_size
        self.items.insert(self.rear, item)
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        item = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items[self.front]


    def length(self):
        return self.size


new_circular_queue = CircularQueue()
new_circular_queue.enqueue(1)
new_circular_queue.enqueue(2)
new_circular_queue.enqueue(3)
print(new_circular_queue.peek())
print(f"Length: {new_circular_queue.length()}")
print(new_circular_queue.dequeue())
print(new_circular_queue.peek())
print(f"Length: {new_circular_queue.length()}")
new_circular_queue.enqueue(4)
print(new_circular_queue.peek())
print(f"Length: {new_circular_queue.length()}")
