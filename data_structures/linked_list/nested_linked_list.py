from data_structures.linked_list.linked_list import *
from data_structures.linked_list.nested_linked_list import *

class NestedLinkedList(LinkedList):
    @staticmethod
    def merge(list1, list2):
        isEmpty = lambda list_to_test: not list_to_test or list_to_test.size == 0

        if isEmpty(list1):
            return list2
        if isEmpty(list2):
            return list1

        list1.sort()
        list2.sort()

        merged = LinkedList()
        list1_node = list1.head
        list2_node = list2.head

        while list1_node is not None or list2_node is not None:
            if list1_node is None:
                merged.append(list2_node)
                list2_node = list2_node.next
            elif list2_node is None:
                merged.append(list1_node)
                list1_node = list1_node.next
            elif list1_node.value <= list2_node.value:
                merged.append(list1_node)
                list1_node = list1_node.next
            elif list2_node.value <= list1_node.value:
                merged.append(list2_node)
                list2_node = list2_node.next
        return merged

    def flatten(self):
        return self.__flatten(self.head)

    def __flatten(self, node):

        if node.next is None:
            return node.value
        return NestedLinkedList.merge(node.value, node.next.value).to_list()

__all__ = ['NestedLinkedList']