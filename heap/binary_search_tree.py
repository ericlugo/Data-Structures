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

    def get_max(self, node=None):
        if node is not None:
            if node.right is not None:
                return node.right.get_max()
            else:
                return node.value
        else:
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

    def in_order_dft(self, node):
        if node.left is not None:
            node.left.in_order_dft(node.left)
        print(node.value)
        if node.right is not None:
            node.right.in_order_dft(node.right)

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

    """
    delete() will remove the given target from the tree if it exists. If there
    are duplicate values within the tree, it will delete the deepest value.
    """

    def delete(self, target):
        target_node = self.get_node(target)
        parent_node = self.get_parent_node(target_node)

        # two children
        if (target_node.left is not None) and (target_node.right is not None):
            # find min value of branch to replace target and store copy of node
            branch_min_value = self.get_min(self.right)
            branch_min_node = self.get_node(branch_min_value)
            # delete min node from current location
            self.delete(branch_min_value)
            # check if target is child or root
            if parent_node is not None:
                # make min node point to target's children
                branch_min_node.left = target_node.left
                branch_min_node.right = target_node.right
                # make target's parent point to min node
                if parent_node.right == target_node:
                    parent_node.right = branch_min_node
                else:
                    parent_node.left = branch_min_node
            # cannot replace root node so transfer value from min node
            else:
                target_node.value = branch_min_value

        # one child - left
        elif target_node.left is not None:
            if parent_node is not None:
                if parent_node.right == target_node:
                    parent_node.right = target_node.left
                else:
                    parent_node.left = target_node.left
            else:
                target_node = target_node.left

        # one child - right
        elif target_node.right is not None:
            if parent_node is not None:
                if parent_node.right == target_node:
                    parent_node.right = target_node.right
                else:
                    parent_node.left = target_node.right
            else:
                target_node = target_node.right

        # no children
        else:
            try:
                if parent_node.right == target_node:
                    parent_node.right = None
                else:
                    parent_node.left = None
            except:
                print(
                    'Cannot delete root node if there are no children to replace it with.')

    def delete_all(self, target):
        while self.contains(target):
            self.delete(target)

    def get_min(self, node=None):
        if node is not None:
            if node.left is not None:
                return node.left.get_min()
            else:
                return node.value
        else:
            if self.left is not None:
                return self.left.get_min()
            else:
                return self.value

    '''
    get_node() will retrieve the node with a value matching the target.
    If there are duplicate values in the tree, always return the deepest
    matching node.
    '''

    def get_node(self, target):
        if self.value == target:
            if self.right and self.right.contains(target):
                return self.right.get_node(target)
            else:
                return self
        elif target < self.value:
            if self.left is None:
                return None
            else:
                return self.left.get_node(target)
        elif self.value < target:
            if self.right is None:
                return None
            else:
                return self.right.get_node(target)

    '''
    get_parent_node() retrieves the parent node of the given target node.
    The actual node is used to account for potential duplicate node values.
    returns the a tuple containing the parent node and a boolean that
    represents (parent <= child)
    '''

    def get_parent_node(self, target_node):
        if self == target_node:
            return None
        elif target_node.value < self.value:
            if self.left is None:
                return None
            elif self.left == target_node:
                return self
            else:
                return self.left.get_parent_node(target_node)
        elif self.value <= target_node.value:
            if self.right is None:
                return None
            elif self.right == target_node:
                return self
            else:
                return self.right.get_parent_node(target_node)
