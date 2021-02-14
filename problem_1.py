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
        if self.size == 0:
            return None

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

    # test case 1 -> size of 0
    LRU_cache = LRUCache(0)
    LRU_cache.set(1, 'a')
    print(LRU_cache.list.to_list()) # expect []
    assert(LRU_cache.get(1) == -1)

    LRU_cache = LRUCache(5)

    LRU_cache.set(1, 'a')
    LRU_cache.set(2, 'b')
    LRU_cache.set(3, 'c')
    LRU_cache.set(4, 'd')

    # test case 2 -> size of 5
    print(
        'After insertion, the cache content is (from oldest to most recent):',
        LRU_cache.list.to_list()
    ) # prints [(1, 1), (2, 2), (3, 3), (4, 4)], with items in order of insertion
    assert(LRU_cache.list.to_list() == [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')])


    # checks correct returns for present and absent files, and also that items are moved at the end of the
    # queue as they are "used"
    assert(LRU_cache.get(1) == 'a')  # returns 1
    assert(LRU_cache.get(2) == 'b')  # returns 2
    assert(LRU_cache.get(9) == -1) # returns -1 (not present)
    print(
        'After using the oldest items in the cache, the cache content is (from oldest to most recent):',
        LRU_cache.list.to_list()
    ) # prints [(3, 3), (4, 4), (1, 1), (2, 2)] as 1 and 2 are moved at the end of the queue
    assert(LRU_cache.list.to_list() == [(3, 'c'), (4, 'd'), (1, 'a'), (2, 'b')])

    # checks that, when full capacity is reached, the lest recent item is removed
    LRU_cache.set(5, 'd')
    LRU_cache.set(6, 'e')
    assert(LRU_cache.get(3) == -1) # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    print(
        'After reaching full capacity and removing the oldest item for adding new items, the cache is (from oldest to most recent):',
        LRU_cache.list.to_list()
    ) # prints [(4, 4), (1, 1), (2, 2), (5, 5), (6, 6)]) as 3 has been removed and 5 and 6 have been recently added
    assert(LRU_cache.list.to_list() == [(4, 'd'), (1, 'a'), (2, 'b'), (5, 'd'), (6, 'e')])

    # test case 3 -> high size
    LRU_cache = LRUCache(1000)
    for i in range(1000):
        LRU_cache.set(i, i)

    # not printing the LRU cache list as it would require quite some space on screen
    print('this LRU_cache is big, for the sake of clarity we can skip printing its list')
    print(
        'After adding items in the cache, the most recent item is the last added:',
        LRU_cache.list.to_list()[999]
    ) # prints (999, 999) as it was the last recently used
    assert(LRU_cache.list.to_list()[999] == (999, 999))


    # checks correct returns for present and absent files, and also that items are moved at the end of the
    # queue as they are "used"
    assert(LRU_cache.get(0) == 0)  # returns 1
    assert(LRU_cache.get(1) == 1)  # returns 2
    assert(LRU_cache.get(1000) == -1) # returns -1 (not present)
    print(
        'After using the oldest items in the cache, now the oldest item is:',
        LRU_cache.list.to_list()[0]
    ) # prints (2, 2) as 0 and 1 have been moved at the end
    assert(LRU_cache.list.to_list()[0] == (2, 2))

    print(
        'After using the oldest item in the cache, now the most recent item is:',
        LRU_cache.list.to_list()[999]
    ) # prints (1, 1) as it was the last recently used
    assert(LRU_cache.list.to_list()[999] == (1, 1))

    # checks that, when full capacity is reached, the lest recent item is removed
    LRU_cache.set(1000, 1000)
    assert(LRU_cache.get(2) == -1) # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    print(
        'After reaching full capacity and removing the oldest items for adding new items, the cache oldest item is',
        LRU_cache.list.to_list()[0]
    ) # prints (3, 3)
    assert(LRU_cache.list.to_list()[0] == (3, 3))
