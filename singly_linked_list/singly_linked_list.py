class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def remove_head(self):
        if (self.length == 0):
            return None
        else:
            deleted_value = self.head.value
            if (self.length == 1):
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            self.length -= 1
            return deleted_value

    def add_to_tail(self, value):
        if (self.length == 0):
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = ListNode(value)
            self.tail = self.tail.next
        self.length += 1

    def contains(self, value):
        match = False
        marker = self.head
        while marker != None:
            if marker.value == value:
                match = True
            marker = marker.next
        return match

    def get_max(self):
        if (self.length == 0):
            return None
        elif (self.length == 1):
            return self.head.value
        else:
            current_node = self.head.next
            highest_value = self.head.value
            while current_node:
                if current_node.value > highest_value:
                    highest_value = current_node.value
                current_node = current_node.next
            return highest_value

    def find_middle(self):
        middle = self.head
        end = self.head
        while end.next != None and end.next.next != None:
            end = end.next.next
            middle = middle.next
        return middle
