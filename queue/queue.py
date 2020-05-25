"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. [x] Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. [x] Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. [ ] What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

from doubly_linked_list import DoublyLinkedList as DLL


class Queue:
    def __init__(self):
        # self.size = 0
        # self.storage = []
        self.storage = DLL()

    def __len__(self):
        # return self.size
        return len(self.storage)

    def enqueue(self, value):
        # self.size = self.size + 1
        # self.storage.append(value)
        self.storage.add_to_tail(value)

    def dequeue(self):
        # if self.size is not 0:
        #     first_in = self.storage[0]
        #     self.size = self.size - 1
        #     self.storage.pop(0)
        #     return first_in
        # else:
        #     return None
        return self.storage.remove_from_head()
