# TASK 5 EXPLANATION

To create a blockchain:

1) We first hash its content: the hashing functions is out the Block class because is a pure function
and has no need to be tied to the state of a Block instance

2) This Block class extends Node, adding properties as per requirements

3) A BlockChain class extends LinkedList, that filters out empty or null values, as they cannot be hashed in the ctor

Time complexity for building a BlockChain is O(n), as we have to iterate over all input values to add them to the chain.

Regarding space complexity, the data structure used in this project (a linked list) allows for a space complexity of O(n),
where n is the number of nodes (or, in this case, blocks) it contains
