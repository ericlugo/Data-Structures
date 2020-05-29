from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.node_count = 0
        self.storage = DoublyLinkedList()
        self.dictionary = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    # if key does not exist
    #     return None
    # otherwise
    #     locate node in storage
    #     move_to_front of storage
    # return value from dictionary[key]
    def get(self, key):
        if (key not in self.dictionary):
            return None
        node_to_move = self.storage.head
        while node_to_move is not None:
            if (node_to_move.value[0] == key):
                self.storage.move_to_front(node_to_move)
                break
            node_to_move = node_to_move.next
        return self.dictionary[key]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    # if key exists
    #     locate node in storage
    #     update value[1] in node
    #     move_to_front of storage
    #     cache node_count does not change
    # if not
    #     if size == limit
    #         Remove_from_tail in storage
    #         Also, pop from dictionary
    #         cache node_count decreases
    #     add_to_head of storage
    #     cache node_count increases
    # write new values to, or overwrite existing values in, dictionary
    def set(self, key, value):
        if (key in self.dictionary):
            node_to_move = self.storage.head
            while node_to_move is not None:
                if (node_to_move.value[0] == key):
                    node_to_move.value[1] = value
                    self.storage.move_to_front(node_to_move)
                    break
                node_to_move = node_to_move.next
        else:
            if (self.node_count == self.limit):
                deleted_node = self.storage.remove_from_tail()
                self.dictionary.pop(deleted_node[0])
                self.node_count -= 1
            self.storage.add_to_head([key, value])
            self.node_count += 1
        self.dictionary[key] = value
