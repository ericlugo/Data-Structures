"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

import sys
from queue import Queue as Q
from stack import Stack as S


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if (value < self.value):
            if (self.left is None):
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if (self.right is None):
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if (target == self.value):
            return True
        if (target < self.value):
            if (self.left is None):
                return False
            else:
                return self.left.contains(target)
        else:
            if (self.right is None):
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if (self.right is None):
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if (self.left is not None):
            self.left.for_each(fn)
        if (self.right is not None):
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # left
        if (node.left is not None):
            node.left.in_order_print(node.left)
        # root
        print(node.value)
        # right
        if (node.right is not None):
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        traversal_queue = Q()
        current_node = node
        while current_node is not None:
            if (current_node.left is not None):
                traversal_queue.enqueue(current_node.left)
            if (current_node.right is not None):
                traversal_queue.enqueue(current_node.right)
            print(current_node.value)
            current_node = traversal_queue.dequeue()

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        traversal_queue = S()
        current_node = node
        while current_node is not None:
            if (current_node.left is not None):
                traversal_queue.push(current_node.left)
            if (current_node.right is not None):
                traversal_queue.push(current_node.right)
            print(current_node.value)
            current_node = traversal_queue.pop()

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # root
        print(node.value)
        # left
        if (node.left is not None):
            node.left.pre_order_dft(node.left)
        # right
        if (node.right is not None):
            node.right.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # left
        if (node.left is not None):
            node.left.post_order_dft(node.left)
        # right
        if (node.right is not None):
            node.right.post_order_dft(node.right)
        # root
        print(node.value)
