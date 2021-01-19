import hashlib
import datetime
from data_structures.linked_list import *

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


if __name__ == '__main__':

    # test case 1 -> blockchain of non-false values
    block_chain = BlockChain('block 1', 'block 2', 'block 3', 'block 1', 'block 2', 'block 3')

    previous_hash = None
    for block in block_chain:
        print(block)
        if block.previous_hash and previous_hash:
            assert(block.previous_hash == previous_hash)
        previous_hash = block.hash

    assert(block_chain.to_list() == expected_output)
    print(block_chain.to_list()) #expects ['block 1', 'block 2', 'block 3'], 'block 1', 'block 2', 'block 3']


    # test case 2 -> blockchain does not store empty values
    block_chain = BlockChain('', '')

    previous_hash = None
    for block in block_chain:
        print(block)
        if block.previous_hash and previous_hash:
            assert(block.previous_hash == previous_hash)
        previous_hash = block.hash

    assert(block_chain.to_list() == expected_output)
    print(block_chain.to_list()) #expects []


    # test case 3 -> blockchain does not store null values
    block_chain = BlockChain(None, None)

    previous_hash = None
    for block in block_chain:
        print(block)
        if block.previous_hash and previous_hash:
            assert(block.previous_hash == previous_hash)
        previous_hash = block.hash

    assert(block_chain.to_list() == expected_output)
    print(block_chain.to_list()) #expects []


    # test case 4 -> blockchain accepts non-string types
    block_chain = BlockChain(True, 1, 0)

    previous_hash = None
    for block in block_chain:
        print(block)
        if block.previous_hash and previous_hash:
            assert(block.previous_hash == previous_hash)
        previous_hash = block.hash

    assert(block_chain.to_list() == expected_output)
    print(block_chain.to_list()) #expects [True, 1 ,0]


