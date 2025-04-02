class Stack:
    def __init__(self, maxsize=0):
        self.stack = []
        self.maxsize = maxsize

    def push(self, value):
        if self.maxsize > self.size() or self.maxsize == 0:
            self.stack.append(value)
        else:
            return "Stack Overflow"
    
    def pop(self):
        if not self.is_empty():
            value = self.stack.pop()
            return value
        return "Stack Underflow"
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is Empty"
    
    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def __str__(self):
        values = "" 
        for value in self.stack[::-1]:
            values += f"| {value} |\n" + " ====\n"
        return values

    
stack = Stack()
for value in range(10):
    stack.push(value)
print(stack)