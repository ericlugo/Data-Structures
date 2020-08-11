from singly_linked_list import LinkedList
from stack import Stack


class Queue:
    def __init__(self):
        # PYTHON'S BUILT-IN LIST
        # self.size = 0
        # self.storage = []

        # SINGLY LINKED LIST
        # self.storage = LinkedList()

        # STACK
        self.storage = Stack()
        self.buffer = Stack()

    def __len__(self):
        # PYTHON'S BUILT-IN LIST
        # return self.size

        # SINGLY LINKED LIST AND STACK
        return len(self.storage)

    def enqueue(self, value):
        # PYTHON'S BUILT-IN LIST
        # self.size += 1
        # self.storage.append(value)

        # SINGLY LINKED LIST
        # self.storage.add_to_tail(value)

        # STACK
        self.storage.push(value)

    def dequeue(self):
        # PYTHON'S BUILT-IN LIST
        # if self.size == 0:
        #     return None
        # else:
        #     first_in = self.storage[0]
        #     self.size -= 1
        #     self.storage.pop(0)
        #     return first_in

        # SINGLY LINKED LIST
        # return self.storage.remove_from_head()

        # STACK
        if len(self.storage) == 0:
            return None
        else:
            for _ in range(len(self.storage)-1):
                self.buffer.push(self.storage.pop())
            dequeued_value = self.storage.pop()
            for _ in range(len(self.buffer)):
                self.storage.push(self.buffer.pop())
            return dequeued_value
