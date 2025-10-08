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
    

def valid_brackets(input_string):
    stack = Stack()
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in input_string:
        if char in bracket_map.values():
            stack.push(char)
        elif char in bracket_map.keys():
            if stack.is_empty() or stack.pop() != bracket_map[char]:
                return False
    
    return stack.is_empty()

print(valid_brackets("()"))
print(valid_brackets("()[]{}"))
print(valid_brackets("(]"))
print(valid_brackets("([)]"))
print(valid_brackets("{[]}"))
print(valid_brackets("((()))"))