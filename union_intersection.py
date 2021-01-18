"""
TASK EXPLANATION
To obtain a the linked list resulting from the union of two linked lists:
1) all node values where added to a set, thus resulting in a set of unique values from both lists
2) then, each value in the set is given to a Node wich is appended to a new linked list

Given input n as the sum of all nodes from both lists, time complexity is (assuming, at worst, each node value is unique)
O(n). This is because of our need to traverse each list for adding node values to the set

Appending values stored in the set to the new list as a time complexity of O(1) as we mantain a reference in the LinkedList class to its tail
Thus, for appending a value there is no need to traverse te list

Overall, time complexity is O(n)

--------

To obtain a the linked list resulting from the intersection of two linked lists:
1) two sets were used to store the node values of one of the two linked lists. The use of a set allows us to avoid issues
with multiple identical values.

2) We iterare over one of the set, and if the current value is also present in the other set then it is added to a third set (representing the intersection)

3) We iterater over the instersection set to add the values to a new linked list

Overall, the same considerations written above are valid for this function. Time complexity is O(n)
"""


from data_structures.linked_list.linked_list import *


def union(llist_1, llist_2):
    union_set = set()
    for node in llist_1:
        union_set.add(node.value)

    for node in llist_2:
        union_set.add(node.value)
    merged = LinkedList()

    for value in union_set:
        merged.append(value)

    return merged


def intersection(llist_1, llist_2):
    ll1_set = set()
    ll2_set = set()
    intersect_set = set()

    for node in llist_1:
        ll1_set.add(node.value)

    for node in llist_2:
        ll2_set.add(node.value)

    for node in llist_1:
        if node.value in ll1_set and node.value in ll2_set:
            intersect_set.add(node.value)

    intersect_list = LinkedList()
    for value in intersect_set:
        intersect_list.append(value)

    return intersect_list

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = []

print('\nelements in first list:', element_1)
print('elements in second list:', element_2)

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

union_list = union(linked_list_1,linked_list_2)
intersect_list = intersection(linked_list_1,linked_list_2)

print ('union: ', union_list.to_list())
print ('intersection: ', intersect_list.to_list())

assert(union_list.to_list() == []) ## empty lists, empty union
assert(intersect_list.to_list() == []) ## empty lists, empty intersection


# Test case 2

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = [3, 4, 5, 6, 7, 8]

print('\nelements in first list:', element_1)
print('elements in second list:', element_2)

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

union_list = union(linked_list_1,linked_list_2)
intersect_list = intersection(linked_list_1,linked_list_2)

print ('union: ', union_list.to_list())
print ('intersection: ', intersect_list.to_list())

assert(union_list.to_list() == element_2) ## one list empty, union is just the not-empty list
assert(intersect_list.to_list() == []) ## one list empty, empty intersection



# Test case 3

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [1, 2, 3, 4, 5]
element_2 = [3, 4, 5, 6, 7, 8, 9, 10]


print('\nelements in first list:', element_1)
print('elements in second list:', element_2)

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

union_list = union(linked_list_1,linked_list_2)
intersect_list = intersection(linked_list_1,linked_list_2)

print ('union: ', union_list.to_list())
print ('intersection: ', intersect_list.to_list())

assert(union_list.to_list() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
assert(intersect_list.to_list() == [3, 4, 5])

