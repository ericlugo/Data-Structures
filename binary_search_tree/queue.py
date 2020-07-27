from singly_linked_list import LinkedList


class Queue:
    def __init__(self):
        self.storage = LinkedList()

    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        return self.storage.remove_from_head()
