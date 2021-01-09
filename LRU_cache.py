"""
TASK EXPLANATION
In order to build a Least Recently Used Cache with  O(1) set and get operations, two data structures are required:
1) a double linked list, in which each node is moved to the tail when their value is required
2) a hash map, allowing to get the node of interest without traversing the list
"""

from data_structures.linked_list.double_linked_list import *


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


LRU_cache = LRUCache(5)

LRU_cache.set(1, 1)
LRU_cache.set(2, 2)
LRU_cache.set(3, 3)
LRU_cache.set(4, 4)
print(LRU_cache.list.to_list())
assert(LRU_cache.list.to_list() == [(1, 1), (2, 2), (3, 3), (4, 4)])


assert(LRU_cache.get(1) == 1)  # returns 1
assert(LRU_cache.get(2) == 2)  # returns 2
assert(LRU_cache.get(9) == -1) # returns -1 (not present)
print(LRU_cache.list.to_list())
assert(LRU_cache.list.to_list() == [(3, 3), (4, 4), (1, 1), (2, 2)])

LRU_cache.set(5, 5)
LRU_cache.set(6, 6)
assert(LRU_cache.get(3) == -1) # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(LRU_cache.list.to_list())
assert(LRU_cache.list.to_list() == [(4, 4), (1, 1), (2, 2), (5, 5), (6, 6)])

assert(LRU_cache.get(4) == 4)  # returns 4
print(LRU_cache.list.to_list())
assert(LRU_cache.list.to_list() == [(1, 1), (2, 2), (5, 5), (6, 6), (4, 4)])

assert(LRU_cache.get(6) == 6)  # returns 6
print(LRU_cache.list.to_list())
assert(LRU_cache.list.to_list() == [(1, 1), (2, 2), (5, 5), (4, 4), (6, 6)])
