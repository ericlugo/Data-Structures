from queue import Queue
from stack import Stack


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif self.value <= value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        elif self.value < target:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    def get_max(self):
        if self.right is not None:
            return self.right.get_max()
        else:
            return self.value

    def for_each(self, fn):
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    def in_order_print(self, node):
        if node.left is not None:
            node.left.in_order_print(node.left)
        print(node.value)
        if node.right is not None:
            node.right.in_order_print(node.right)

    def bft_print(self, node):
        bft_queue = Queue()
        current_node = node
        while current_node is not None:
            if current_node.left is not None:
                bft_queue.enqueue(current_node.left)
            if current_node.right is not None:
                bft_queue.enqueue(current_node.right)
            print(current_node.value)
            current_node = bft_queue.dequeue()

    def dft_print(self, node):
        dft_stack = Stack()
        current_node = node
        while current_node is not None:
            if current_node.left is not None:
                dft_stack.push(current_node.left)
            if current_node.right is not None:
                dft_stack.push(current_node.right)
            print(current_node.value)
            current_node = dft_stack.pop()

    # Stretch Goals -------------------------

    def pre_order_dft(self, node):
        print(node.value)
        if node.left is not None:
            node.left.pre_order_dft(node.left)
        if node.right is not None:
            node.right.pre_order_dft(node.right)

    def post_order_dft(self, node):
        if node.left is not None:
            node.left.post_order_dft(node.left)
        if node.right is not None:
            node.right.post_order_dft(node.right)
        print(node.value)
