class Heap:
    def __init__(self):
        self.storage = []

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    # PRIMARY HEAP FUNCTIONALITY ===============================
    '''
    insert() adds the input value into the heap; this method
    should ensure that the inserted value is in the correct spot
    in the heap
    '''

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(self.get_size()-1)

    '''
    delete() removes and returns the 'topmost' value from the
    heap; this method needs to ensure that the heap property is
    maintained after the topmost element has been removed.
    '''

    def delete(self):
        max_value = self.storage[0]
        self.storage[0] = self.storage[self.get_size()-1]
        self.storage.pop(self.get_size()-1)
        self._sift_down(0)
        return max_value

    '''
    _bubble_up() moves the element at the specified index "up"
    the heap by swapping it with its parent if the parent's value
    is less than the value at the specified index.
    '''

    def _bubble_up(self, index):
        i = index
        while _need_to_bubble(self.storage, i):
            parent = self.storage[_p(i)]
            self.storage[_p(i)] = self.storage[i]
            self.storage[i] = parent
            i = _p(i)

    '''
    _sift_down() grabs the indices of this element's children and
    determines which child has a larger value. If the larger
    child's value is larger than the parent's value, the child
    element is swapped with the parent.
    '''

    def _sift_down(self, index):
        i = index
        while _need_to_sift(self.storage, i):
            left = self.storage[_l(i)] if _l(i) <= len(self.storage)-1 else None
            right = self.storage[_r(i)] if _r(i) <= len(self.storage)-1 else None
            if left is not None and right is not None:
                if left < right:
                    self.storage[_r(i)] = self.storage[i]
                    self.storage[i] = right
                    i = _r(i)
                else:
                    self.storage[_l(i)] = self.storage[i]
                    self.storage[i] = left
                    i = _l(i)
            else:
                if left is not None:
                    self.storage[_l(i)] = self.storage[i]
                    self.storage[i] = left
                    i = _l(i)
                elif right is not None:
                    self.storage[_r(i)] = self.storage[i]
                    self.storage[i] = right
                    i = _r(i)


"""
GENERAL NOTES:

A Max Heap is:
    an implementation of a Priority Queue abstract data type
        A Priority Queue can:
            is_empty()
            insert_with_priority()
            pull_highest_priority_item()
            peek()
    a complete balanced binary tree
        (balanced trees are filled Left-to-Right and Top-to-Bottom)
"""

# AUXILLARY FUNCTIONS ==========================================
def _p(i):
    return int((i-1)/2)


def _l(i):
    return (2*i)+1


def _r(i):
    return (2*i)+2


def _need_to_bubble(store, i):
    if 1 < len(store):
        if i == 0:
            return False
        else:
            parent = store[_p(i)]
            node = store[i]
            if parent < node:
                return True
            else:
                return False
    else:
        return False


def _need_to_sift(store, i):
    if 1 < len(store):
        node = store[i]
        left = store[_l(i)] if (_l(i) <= len(store)-1) else None
        right = store[_r(i)] if (_r(i) <= len(store)-1) else None
        if (left is not None) and (node < left):
            return True
        elif (right is not None) and (node < right):
            return True
        else:
            return False
    else:
        return False
