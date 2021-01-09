
from data_structures.linked_list.linked_list import *

class DoubleNode(Node):

    def __init__(self, value):
        super().__init__(value)
        self.previous: DoubleNode = None


class DoublyLinkedList(LinkedList):

    head: DoubleNode = None
    tail: DoubleNode = None
    _size: int = 0

    def __init__(self, *args):
        super().__init__(*args)

    def move_to_tail(self, node: DoubleNode):
        if node is self.tail:
            return

        if node is self.head:
            self._move_head_to_tail()
        else:
            node.previous.next = node.next
            node.next.previous = node.previous
            self._append_node(node)

    def _init_head(self, value):
        self.head = DoubleNode(value)
        self.tail = self.head

    def _append(self, value):
        node_to_append = DoubleNode(value)
        node_to_append.previous = self.tail
        self.tail.next = node_to_append
        self.tail = node_to_append

    def _append_node(self, node: DoubleNode):
        node.previous = self.tail
        self.tail.next = node
        self.tail = node
        self.tail.next = None

    def _move_head_to_tail(self):
        self.tail.next = self.head
        self.head.previous = self.tail
        self.head = self.head.next
        self.head.previous = None
        self.tail = self.tail.next
        self.tail.next = None

    def _prepend(self, value):
        node_to_prepend = DoubleNode(value)
        self.head.previous = node_to_prepend
        node_to_prepend.next = self.head
        self.head = node_to_prepend

    def _insert(self, value, pos: int):
        currentPosition = 0
        pos -= 1
        for node in self:
            if pos == currentPosition:
                node_to_insert = DoubleNode(value)
                node_to_insert.next = node.next
                node_to_insert.previous = node
                node.next = node_to_insert
                break
            currentPosition += 1

    def _pop(self):
        node_to_remove = self.head
        value_to_return = node_to_remove.value
        self.head = self.head.next
        self.head.previous = None
        del node_to_remove
        return value_to_return


__all__ = ['DoublyLinkedList', 'DoubleNode']
