class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []
        self.exists = [0] * size

    def push(self, item):
        if self.is_full():
            raise ValueError("Stack is full!")
        self.stack.append(item)
        self.exists[item - 1] = 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty!")
        item = self.stack.pop()
        self.exists[item - 1] = 0
        return item

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.size