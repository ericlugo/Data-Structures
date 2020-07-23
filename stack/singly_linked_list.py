from sll_node import SLL_Node


class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_tail(self, value):
        new_node = SLL_Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1

    def remove_from_tail(self):
        if self.length == 0:
            return None
        else:
            value = self.tail.get_value()
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                current_node = self.head
                while current_node is not None:
                    if current_node.get_next() == self.tail:
                        self.tail = current_node
                        current_node.set_next(None)
                    current_node = current_node.get_next()
            self.length -= 1
            return value
