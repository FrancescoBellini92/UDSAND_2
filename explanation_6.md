# TASK 6 EXPLANATION

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
