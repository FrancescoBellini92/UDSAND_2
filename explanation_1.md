
# TASK 1 EXPLANATION

In order to build a Least Recently Used Cache with  O(1) set and get operations, two data structures are required:

1) a double linked list, in which each node is moved to the tail when their value is required
2) a hash map, allowing to get the node of interest without traversing the list

The logic is to move an item to the end of the list each time it is "used".
Therefore, removing the least-recently used item as a complexity of O(1) since we mantain a reference to the list head
To avoid traversing the list each time we need to move a node to the end of the list, as stated above, we use a hash map
with key-node associations.

The time complexity of moving a node to the endo of the list is also O(1), as only requires linking its neighbours together
and moving it to the tail of the list (of which we maintain a reference)

Overall, each operation has a time complexity of O(1)

In terms of space complexity, it's equal to the size of the cache ( O(n) ), as:
1) we have up to n nodes in the cache linked list
2) the hash table would also mantain pointers tho those nodes
