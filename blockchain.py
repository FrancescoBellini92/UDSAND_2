import hashlib
import datetime
from data_structures.linked_list.linked_list import *

""" TASK EXPLANATION
To create a blockchain:

1) We first hash its content: the hashing functions is out the Block class because is a pure function
and has no need to be tied to the state of a Block instance

2) This Block class extends Node, adding properties as per requirements

3) A BlockChain class extends LinkedList, that filters out empty or null values, as they cannot be hashed in the ctor

Time complexity for building a BlockChain is O(n), as we have to iterate over all input values to add
them to the chain.

"""


def calc_hash_from_string(data):
    sha = hashlib.sha256()
    sha.update(str(data).encode('utf-8'))

    return sha.hexdigest()


class Block(Node):

    def __init__(self, value, previous_hash = None, timestamp = datetime.datetime.utcnow()):
        super().__init__(value)
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = calc_hash_from_string(value)


    def __repr__(self):

        return 'block %s | data: %s | timestamp: %s | previous: %s' %(self.hash, self.value, self.timestamp, self.previous_hash)


class BlockChain(LinkedList):

    def __init__(self, *args):
        args = filter(lambda item: item is not None and item is not '', args)
        super().__init__(*args)

    def _append(self, data):
        node_to_append = Block(data, self.tail.hash)
        super()._append_node(node_to_append)

    def _init_head(self, value):
        self.head = Block(value)
        self.tail = self.head

def test_blockchain(expected_output, *args):
    block_chain = BlockChain(*args)

    previous_hash = None
    for block in block_chain:
        print(block)
        if block.previous_hash and previous_hash:
            assert(block.previous_hash == previous_hash)
        previous_hash = block.hash

    assert(block_chain.to_list() == expected_output)

if __name__ == '__main__':
    test_blockchain(['block 1', 'block 2', 'block 3'], 'block 1', 'block 2', 'block 3') # test case 1 -> blockchain accepts non-empty strings
    test_blockchain([], '', '') # test case 2 -> blockchain does not store empty values
    test_blockchain([], None, None) # test case 3 -> blockchain does not store null values
    test_blockchain([True, 1, 0], True, 1, 0) # test case 4 -> blockchain accepts non-string types


