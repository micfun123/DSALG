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
    


def remove_ajacent_dupes(input_string):
    stack = Stack()
    for char in input_string:
        if not stack.is_empty() and stack.peek() == char:
            stack.pop()
        else:
            stack.push(char)
    
    result = ''
    while not stack.is_empty():
        result = stack.pop() + result
    
    return result


print(remove_ajacent_dupes("abbccd"))
print(remove_ajacent_dupes("dsallasg"))
print(remove_ajacent_dupes("abccbadd"))