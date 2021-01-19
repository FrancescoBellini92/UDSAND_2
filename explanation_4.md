# TASK 4 EXPLANATION

The Group class allows for the creation of a hierarchy of users and gruoups, similarly to a n-tree structure.

In this case, the search was implemented with a breadth-first traversal, as it made more sense to me that
a given user was searched in such a way rather than with a depth-first approach

To increase efficiency, a set was used for storing user IDs (which should work as long as they are unique)

Overall, the time complexity is O(n), as we have to visit each node of the tree (each group)

The breadth first search was implemented with a queue and a while loop,returning when the user is found

In case of user belonging to multiple groups, the first group is returned
