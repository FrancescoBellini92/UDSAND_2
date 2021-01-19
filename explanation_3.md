TASK 3 EXPLANATION
In this task two data structures are used:
1- a double linked list
2- a binary tree

Given input n as the length of the string:

1) We start by traversing the string to decode to create a character-frequency map, which will be used to populate the linked list
These operations require traversing the string ( time complexity of O(n) ), and updating the character-frequency map (time complexity of O(1) )

2) Then, the list is traversed n times to find the two nodes with smaller frequency value to create the Huffman tree,
Time complexity depends in this case on:
- the traversing of the list ( O(n) )
- the removal of the node ( O(1) )
- the instantiation of a TreeNode ( O(1) )
- the prepending operation of the newly instantiated TreeNode to the linked list ( O(1) )

Overall, the time complexity for a single function call is O(n). The recursive calls results in an overall time complexity
of O(n + (n - 1) + (n -2) + ... 1) -> O(n)

3) We create the a char-prefix map (for encoding the string) and a prefix_char map (to decode the encoded string) via a depth first traversal on the huffman tree,
mapping each character to its prefix code and viceversa.
Considering that the huffman tree is a binary tree, and at worst case each character is unique, we would end up with a tree that has 2n - 1 nodes
Thus the overall time complexity of the tree traversal is O(n). Saving data in the hash maps takes O(1) time

4) We iterare on the original string to convert each character with its prefix thanks the char-prefix map. The complexity is O(n)

5) For decoding, we iterate over each character in the encoded string and perform a lookup in a hash map
This final operation has a time complexity of O(n)

Overall, the time complexity of the whole procedure is O(n)
