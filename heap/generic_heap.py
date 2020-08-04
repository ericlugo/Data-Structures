class Heap:
    def __init__(self, comparator = lambda x, y : x > y):
        self.storage = []
        self.comparator = comparator

    # return Priority Queue's top node (current priority)
    def get_priority(self):
        return self.storage[0]

    # return size of Priority Queue
    def get_size(self):
        return len(self.storage)

    # PRIMARY HEAP FUNCTIONALITY ===============================
    
    # Add value to end of Priority Queue and trigger bubbling
    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(self.get_size()-1)

    # Remove priority node from Queue and trigger sifting
    def delete(self):
        priority = self.storage[0]
        self.storage[0] = self.storage[self.get_size()-1]
        self.storage.pop(self.get_size()-1)
        self._sift_down(0)
        return priority

    # moves the node "up" in the Priority Queue if the
    # comparator's conditions are met
    def _bubble_up(self, index):
        i = index
        while _need_to_bubble(self.storage, i, self.comparator):
            parent = self.storage[_p(i)]
            self.storage[_p(i)] = self.storage[i]
            self.storage[i] = parent
            i = _p(i)

    # moves the node "down" in the  Priority Queue if the
    # comparator's conditions are met
    def _sift_down(self, index):
        i = index
        while _need_to_sift(self.storage, index, self.comparator):
            left = self.storage[_l(i)] if _l(i) <= len(self.storage)-1 else None
            right = self.storage[_r(i)] if _r(i) <= len(self.storage)-1 else None
            if left is not None and right is not None:
                # if left < right:
                if self.comparator(right, left):
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

# AUXILLARY FUNCTIONS ==========================================
def _p(i):
    return int((i-1)/2)


def _l(i):
    return (2*i)+1


def _r(i):
    return (2*i)+2

def _need_to_bubble(store, i, comparator):
    if 1 < len(store):
        if i == 0:
            return False
        else:
            parent = store[_p(i)]
            node = store[i]
            if comparator(node, parent):
                return True
            else:
                return False
    else:
        return False

def _need_to_sift(store, i, comparator):
    if 1 < len(store):
        node = store[i]
        left = store[_l(i)] if (_l(i) <= len(store)-1) else None
        right = store[_r(i)] if (_r(i) <= len(store)-1) else None
        # if (left is not None) and (node < left):
        if (left is not None) and comparator(left, node):
            return True
        # elif (right is not None) and (node < right):
        elif (right is not None) and comparator(right, node):
            return True
        else:
            return False
    else:
        return False
