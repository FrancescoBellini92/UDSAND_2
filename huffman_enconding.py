
import sys
from data_structures.linked_list.double_linked_list import *

"""
TASK EXPLANATION
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
"""
class TreeNode(DoubleNode):
    def __init__(self, value = None):
        super().__init__(value)
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value[1])

class HuffmanTree:
    def __init__(self, root):
        self.root = root
        self.char_prefix_map = {}
        self.prefix_char_map = {}

    def get_prefix_map(self):
        self.char_prefix_map = {}

        def _traverse(node, prefix_code = ''):
            if isinstance(node, TreeNode):
                if node.left:
                    _traverse(node.left, prefix_code + '0')
                if node.right:
                    _traverse(node.right, prefix_code + '1')
            else:
                if node is self.root:
                    prefix_code = '1'
                self.char_prefix_map[node.value[0]] = prefix_code
                self.prefix_char_map[prefix_code] = node.value[0]

        _traverse(self.root)
        return self.char_prefix_map

    def __repr__(self):
        traverse_queue = [(self.root, 0)]
        print_queue = []

        while len(traverse_queue) > 0:
            node, level = traverse_queue.pop(0)
            if isinstance(node, TreeNode):
                if node.left:
                    traverse_queue.append((node.left, level + 1))
                if node.right:
                    traverse_queue.append((node.right, level + 1))

            print_queue.append((node, level))

        start_level = -1
        ret = ''
        for node, level in print_queue:
            if level != start_level:
                start_level = level
                ret = ret + '\n'
            else:
                ret = ret + '|'
            ret = ret + node.value[0] + str(node.value[1])

        return ret


def huffman_encoding(data):
    if len(data) == 0:
        return data, None

    queue = _create_linked_list_from_string(data)

    tree = HuffmanTree(_create_tree_from_linked_list(queue))
    prefix_map = tree.get_prefix_map()

    encoded = ''
    for char in data:
        encoded = encoded + prefix_map[char]

    return encoded, tree


def _create_linked_list_from_string(data):
    frequency_map = {}
    queue = DoublyLinkedList()
    for char in data:
        frequency_map.setdefault(char, 0)
        frequency_map[char] += 1

    for char in frequency_map:
        frequency = frequency_map[char]
        queue.append((char, frequency))
    return queue


def _create_tree_from_linked_list(queue):
        if queue.size() == 1:
            return queue.head

        min_node_1 = _get_min_node(queue)
        min_node_2 = _get_min_node(queue)
        nodes_to_merge = [min_node_1, min_node_2]

        freq_1 = nodes_to_merge[0].value[1]
        freq_2 = nodes_to_merge[1].value[1]
        merged = TreeNode(('', freq_1 + freq_2))
        merged.left = nodes_to_merge[0]
        merged.right = nodes_to_merge[1]
        queue.prepend_node(merged)
        return _create_tree_from_linked_list(queue)

def _get_min_node(queue):
    minimun = sys.maxsize
    minimun_node = None
    for node in queue:
        frequency = node.value[1]
        if frequency <= minimun:
            minimun = frequency
            minimun_node = node
    queue.remove_node(minimun_node)
    return minimun_node


def huffman_decoding(data,tree):
    decoded = ''
    char_buffer = ''
    for char in data:
        char_buffer = char_buffer + char
        if char_buffer in tree.prefix_char_map:
            decoded = decoded + tree.prefix_char_map[char_buffer]
            char_buffer = ''

    return decoded


if __name__ == "__main__":

    empty_string = ''
    repeated_char_string = 'aaa'
    a_great_sentence = "The bird is the word"
    test_cases = [empty_string, repeated_char_string, a_great_sentence]
    for string in test_cases:
        print('----------------\ntest case: %s' %string)

        print ("The size of the data is: {}\n".format(sys.getsizeof(string)))
        print ("The content of the data is: {}\n".format(string))

        encoded_data, tree = huffman_encoding(string)
        if encoded_data:

            print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
            print ("The content of the encoded data is: {}\n".format(encoded_data))

            decoded_data = huffman_decoding(encoded_data, tree)
            assert(decoded_data == string)

            print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
            print ("The content of the encoded data is: {}\n".format(decoded_data))
        else:
            assert(len(string) == 0)
            print('empty string, nothing to decode...')