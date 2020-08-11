from sll_node import SLL_Node


class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = SLL_Node(value, self.head)
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1

    def add_to_tail(self, value):
        new_node = SLL_Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1

    def remove_from_head(self):
        if self.length == 0:
            return None
        else:
            removed_value = self.head.get_value()
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next()
            self.length -= 1
            return removed_value

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

    def contains(self, value):
        match_found = False
        current_node = self.head
        while current_node is not None:
            if current_node.get_value() == value:
                match_found = True
            current_node = current_node.get_next()
        return match_found

    def get_max(self):
        if self.length == 0:
            return None
        current_node = self.head
        max_value = current_node.get_value()
        while current_node is not None:
            if max_value < current_node.get_value():
                max_value = current_node.get_value()
            current_node = current_node.get_next()
        return max_value

    def print_middle(self):
        middle = self.head
        end = self.head
        while end.get_next() != None and end.get_next().get_next() != None:
            end = end.get_next().get_next()
            middle = middle.get_next()
        if self.length % 2 == 0:
            print(
                f'The middle values are: {middle.get_value()} and {middle.get_next().get_value()}')
        else:
            print(f'The middle value of the list is: {middle.get_value()}')

    def print_list(self):
        linked_list_values = []
        current_node = self.head
        while current_node is not None:
            linked_list_values.append(current_node.get_value())
            current_node = current_node.get_next()
        print(f'These are the values of the list: {linked_list_values}')

    def reverse(self):
        iterator = self.head
        current_node = self.head
        previous_node = None

        self.head = self.tail
        self.tail = current_node

        while iterator is not None:
            iterator = iterator.get_next()
            current_node.set_next(previous_node)
            previous_node = current_node
            current_node = iterator


# testing my extra functions
# myList = LinkedList()
# myList.add_to_head(0)
# myList.add_to_head(1)
# myList.add_to_head(2)
# myList.add_to_head(4)
# myList.print_list()
# myList.remove_from_tail()
# myList.print_list()
# myList.print_middle()
# myList.reverse()
# myList.print_list()
# myList.print_middle()
