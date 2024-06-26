class Queue:
    def __init__(self):
        self.items = []

    # check if the stack is empty or not
    def is_empty(self):
        return len(self.items) == 0

    # push a new element onto the stack
    def push(self, item):
        self.items.insert(0, item)

    # pop an element from the stack
    def pop(self):
        if self.is_empty():
            print("There is no element to remove")
            return
        return self.items.pop()

    # print the stack
    def print_queue(self):
        print(self.items)
