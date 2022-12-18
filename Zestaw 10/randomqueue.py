import random

class RandomQueue:

    def __init__(self, size):
        self.size = size
        self.items = []

    def insert(self, item):
        if self.is_full():
            raise ValueError("Queue is full")

        self.items.append(item)

    def remove(self):
        if self.is_empty():
            raise ValueError("Queue is empty")

        index = random.randrange(len(self.items))
        if index == self.size - 1:
            return self.items.pop(index)
        else:
            self.items[index], self.items[-1] = self.items[-1], self.items[index]

            return self.items.pop(index)

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.size

    def clear(self):
        self.items = []