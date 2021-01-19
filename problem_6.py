from data_structures.linked_list import *


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

# Test case 1 -> testing with two empty lists

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

print ('union: ', union_list.to_list()) # expect []
print ('intersection: ', intersect_list.to_list()) # expect []

assert(union_list.to_list() == []) ## empty lists, empty union
assert(intersect_list.to_list() == []) ## empty lists, empty intersection


# Test case 2 -> one list is not empty

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

print ('union: ', union_list.to_list()) # expects [3, 4, 5, 6, 7, 8]
print ('intersection: ', intersect_list.to_list()) # expects []

assert(union_list.to_list() == element_2) ## one list empty, union is just the not-empty list
assert(intersect_list.to_list() == []) ## one list empty, empty intersection


# Test case 3 -> both lists have values

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

print ('union: ', union_list.to_list()) # expect [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print ('intersection: ', intersect_list.to_list()) # expcet [3, 4, 5]

assert(union_list.to_list() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
assert(intersect_list.to_list() == [3, 4, 5])

