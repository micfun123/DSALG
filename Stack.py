
class Stack:
    def __init__(self):
        self.items = []
        self.max_size = 15

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.max_size:
            self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        
    def peek(self):
        return self.items[-1] if not self.is_empty() else None
    
    def length(self):
        return len(self.items)
    
new_stack = Stack()
new_stack.push(1)
new_stack.push(2)
new_stack.push(3)
