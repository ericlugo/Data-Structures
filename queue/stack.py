from singly_linked_list import LinkedList


class Stack:
    def __init__(self):
        # PYTHON'S BUILT-IN LIST
        # self.size = 0
        # self.storage = []

        # SINGLY LINKED LIST
        self.storage = LinkedList()

    def __len__(self):
        # PYTHON'S BUILT-IN LIST
        # return self.size

        # SINGLY LINKED LIST
        return len(self.storage)

    def push(self, value):
        # PYTHON'S BUILT-IN LIST
        # self.storage.append(value)
        # self.size += 1

        # SINGLY LINKED LIST
        self.storage.add_to_tail(value)

    def pop(self):
        # PYTHON'S BUILT-IN LIST
        # if self.size == 0:
        #     return None
        # else:
        #     self.size -= 1
        #     top = self.storage[self.size]
        #     self.storage.pop(self.size)
        #     return top

        # SINGLY LINKED LIST
        return self.storage.remove_from_tail()
