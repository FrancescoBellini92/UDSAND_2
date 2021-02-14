# TASK 6 EXPLANATION

To obtain a linked list resulting from the union of two linked lists:
1) all node values where added to a set, thus resulting in a set of unique values from both lists
2) then, each value in the set is given to a Node wich is appended to a new linked list

Given input n = nodes of list 1 and m = nodes of list 2 and k as n + m:
-For the union of nodes from both lists, time complexity is (assuming, at worst, each node value is unique) O(k).
This is because of our need to traverse each list for adding node values to the set

Appending the k values stored in the set has a time complexity of O(k), as we have to iterate over the set to append nodes to the list.
The appending operation has a time complexity of O(1), as the linked list implementation mantains a reference to its tail and thus allows us to skip
traversing the list.

Time complexity is O(k)

Space complexity of the union procedure is O(k):
- memory of n nodes in list 1
- memory of m nodes in list 2
- memory of k = n + m nodes in list resulting from the union

--------

To obtain a linked list resulting from the intersection of two linked lists:
1) two sets were used to store the node values of one of the two linked lists. The use of a set allows us to avoid issues
with multiple identical values.

2) We iterare over one of the set, and if the current value is also present in the other set then it is added to a third set (representing the intersection)

3) We iterater over the intersection set to add the values to a new linked list

Assuming:
- n as the size of list 1
- m as the size of list 2
- k as n + m
- z as the intersection of n and m

The same considerations written above are valid for for both time and space complexities:
- time complexity is O(k) (since we have to iterare on n and m values)
- space complexity is O(k)
