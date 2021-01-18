class Node:

    def __init__(self, value):
        self.value = value
        self.next: Node = None

    def __repr__(self):
        return str(self.value)


class LinkedList:

    head: Node = None
    tail: Node = None
    _size: int = 0

    def __init__(self, *args):
        for value in args:
            self.append(value)

    def append(self, value):
        """ Append a value to the end of the list. """

        if self.tail is None:
            self._init_head(value)
        else:
            self._append(value)
        self._size += 1

    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """

        if self.head is None:
            self._init_head(value)
        else:
            self._prepend(value)
        self._size += 1

    def prepend_node(self, node):
        """ Prepend a value to the beginning of the list. """

        if self.head is None:
            self.head = node
        else:
            self._prepend_node(node)
        self._size += 1

    def insert(self, value, pos: int):
        """ Insert value at pos position in the list. If pos is larger than the
        length of the list, append to the end of the list. """

        if pos > self._size:
            self._append(value)
        elif pos == 0:
            self._prepend(value)
        else:
            self._insert(value, pos)
        self._size += 1

    def remove(self, value):
        """ Remove first occurrence of value. """

        if self.head and self.head.value == value:
            self._pop()
        else:
            self._remove_after_head(value)
        self._size -= 1

    def pop(self):
        """ Return the first node's value and remove it from the list. """

        popped_value = self._pop()
        self._size -= 1

        return popped_value

    def search(self, value):
        """ Search the linked list for a node with the requested value
        and return the first occurence. """

        for node in self:
            if node.value == value:
                return node

    def to_list(self):
        """ Returns node values as array. """

        acc = []
        for node in self:
            acc.append(node.value)

        return acc

    def reverse(self):
        reversed = LinkedList()
        for node in self:
            reversed.prepend(node.value)
        return reversed

    def clear(self):
        node = self.head
        while node:
            node_to_remove = node
            node = node.next
            del node_to_remove
        self.head = None
        self.tail = None

    def sort(self):
        acc = []
        for node in self:
            acc.append(node.value)
        acc = sorted(acc)

        self.clear()
        for value in acc:
            self.append(value)
        return self

    def size(self):
        """ Returns the number of nodes in the list. """

        return self._size

    def is_circular(self):
        fast_runner = self.head
        slow_runner = self.head

        while fast_runner and fast_runner.next:
            slow_runner = slow_runner.next
            fast_runner = fast_runner.next.next
            if slow_runner == fast_runner:
                return True
        return False

    def _init_head(self, value):
        self.head = Node(value)
        self.tail = self.head

    def _append(self, value):
        self.tail.next = Node(value)
        self.tail = self.tail.next

    def _append_node(self, node):
        self.tail.next = node
        self.tail = node
        self.tail.next = None

    def _prepend(self, value):
        node_to_prepend = Node(value)
        node_to_prepend.next = self.head
        self.head = node_to_prepend

    def _prepend_node(self, node_to_prepend):
        node_to_prepend.next = self.head
        self.head = node_to_prepend

    def _insert(self, value, pos):
        currentPosition = 0
        pos -= 1
        for node in self:
            if pos == currentPosition:
                node_to_insert = Node(value)
                node_to_insert.next = node.next
                node.next = node_to_insert
                break
            currentPosition += 1

    def _pop(self):
        node_to_remove = self.head
        value_to_return = node_to_remove.value
        self.head = self.head.next
        del node_to_remove
        return value_to_return

    def _remove_after_head(self, value):
        for node in self:
            node_to_remove = node.next
            if node_to_remove.value == value:
                node.next = node_to_remove.next
                del node_to_remove
                if node.next is None:
                    self.tail = node
                break

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


__all__ = ['LinkedList', 'Node']