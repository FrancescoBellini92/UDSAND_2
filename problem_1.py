from data_structures.double_linked_list import *


class LRUCache(object):

    def __init__(self, size):
        self.size = size
        self.node_map = {}
        self.numerosity = 0
        self.list = DoublyLinkedList()

    def get(self, key):
        if key in self.node_map:
            node = self.node_map[key]
            self.list.move_to_tail(node)
            return node.value[1]
        return -1

    def set(self, key, value):
        if self._is_full():
            head = self.list.pop()
            del self.node_map[head[0]]

        if key not in self.node_map:
            self.list.append((key, value))
            self.node_map[key] = self.list.tail
            self.numerosity += 1
            return

        node = self.node_map[key]
        self.list.move_to_tail(node)

    def _is_full(self):
        return self.numerosity == self.size

if __name__ == '__main__':
    LRU_cache = LRUCache(5)

    LRU_cache.set(1, 1)
    LRU_cache.set(2, 2)
    LRU_cache.set(3, 3)
    LRU_cache.set(4, 4)
    # test case 1 -> list order of items mirrors that of insertion
    print(LRU_cache.list.to_list()) # prints [(1, 1), (2, 2), (3, 3), (4, 4)], with items in order of insertion
    assert(LRU_cache.list.to_list() == [(1, 1), (2, 2), (3, 3), (4, 4)])


    # test case 3 -> checks correct returns for present and absent files, and also that items are moved at the end of the
    # queue as they are "used"
    assert(LRU_cache.get(1) == 1)  # returns 1
    assert(LRU_cache.get(2) == 2)  # returns 2
    assert(LRU_cache.get(9) == -1) # returns -1 (not present)
    print(LRU_cache.list.to_list()) # prints [(3, 3), (4, 4), (1, 1), (2, 2)] as 1 and 2 are moved at the end of the queue
    assert(LRU_cache.list.to_list() == [(3, 3), (4, 4), (1, 1), (2, 2)])

    # test case 4 -> checks that, when full capacity is reached, the lest recent item is removed
    LRU_cache.set(5, 5)
    LRU_cache.set(6, 6)
    assert(LRU_cache.get(3) == -1) # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    print(LRU_cache.list.to_list()) # prints [(4, 4), (1, 1), (2, 2), (5, 5), (6, 6)]) as 3 has been removed and 5 and 6 have been recently added
    assert(LRU_cache.list.to_list() == [(4, 4), (1, 1), (2, 2), (5, 5), (6, 6)])
