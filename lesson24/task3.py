from collections import deque
class Stack:
    def __init__(self):
        self.items = deque()
        self.item = None

    def push(self, item):
        self.items = [i for i in item]

    def pop(self):
        return self.items.pop()

    def get_from_stack(self, item):
        for i in range(len(self.items)):
            s = self.pop()
            if s == item:
                self.item = s
            else:
                self.items.insert(0, s)
        if self.item == None:
            raise ValueError("No item listed")
        return self.item

lst = [1, 3, 5, 8, 44, 99]
nnn = Stack()
nnn.push(lst)
print(nnn.get_from_stack(5))





