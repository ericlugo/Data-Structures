"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. [x] Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. [x] Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. [ ] What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

from doubly_linked_list import DoublyLinkedList as DLL


class Stack:
    def __init__(self):
        # self.size = 0
        # self.storage = []
        self.storage = DLL()

    def __len__(self):
        # return self.size
        return len(self.storage)

    def push(self, value):
        # self.storage.append(value)
        # self.size = self.size + 1
        self.storage.add_to_tail(value)

    def pop(self):
        # if self.size is not 0:
        #     self.size = self.size - 1
        #     stack_top = self.storage[self.size]
        #     self.storage.pop(self.size)
        #     return stack_top
        # else:
        #     return None
        return self.storage.remove_from_tail()
