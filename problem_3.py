import sys
from data_structures.double_linked_list import *

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

    queue = _create_linked_list_from_string_to_decode(data)

    tree = HuffmanTree(_create_tree_from_linked_list(queue))
    prefix_map = tree.get_prefix_map()

    encoded = ''
    for char in data:
        encoded = encoded + prefix_map[char]

    return encoded, tree


def _create_linked_list_from_string_to_decode(data):
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

    # test case 1 -> empty string_to_decode
    string_to_decode = ''
    expected_encoded_string = ''

    print('----------------\ntest case: %s' %string_to_decode)
    print ("The content of the data is: {}\n".format(string_to_decode)) # expect ''

    encoded_data, tree = huffman_encoding(string_to_decode)
    assert(encoded_data == expected_encoded_string)
    print ("The content of the encoded data is: {}\n".format(encoded_data)) # expect ''

    decoded_data = huffman_decoding(encoded_data, tree)
    assert(decoded_data == string_to_decode)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data)) # expect ''



    # test case 2 -> string of same repeated letters
    string_to_decode = 'aaa'
    expected_encoded_string = '111'
    print('----------------\ntest case: %s' %string_to_decode)
    print ("The content of the data is: {}\n".format(string_to_decode)) # expect 'aaa'

    encoded_data, tree = huffman_encoding(string_to_decode)
    assert(encoded_data == expected_encoded_string)
    print ("The content of the encoded data is: {}\n".format(encoded_data)) # expect '111'

    decoded_data = huffman_decoding(encoded_data, tree)
    assert(decoded_data == string_to_decode)
    print ("The content of the decoded data is: {}\n".format(decoded_data)) # expect 'aaa'


    # test case 3 -> string with different letters
    string_to_decode = 'The bird is the word'
    expected_encoded_string = '1011010001110101000011111110110000100111010000100011100111011011111110'
    print('----------------\ntest case: %s' %string_to_decode)
    print ("The content of the data is: {}\n".format(string_to_decode)) # expect 'The bird is the word'

    encoded_data, tree = huffman_encoding(string_to_decode)
    assert(encoded_data == expected_encoded_string)
    print ("The content of the encoded data is: {}\n".format(encoded_data)) # expect '1011010001110101000011111110110000100111010000100011100111011011111110'

    decoded_data = huffman_decoding(encoded_data, tree)
    assert(decoded_data == string_to_decode)
    print ("The content of the decoded data is: {}\n".format(decoded_data)) # expect 'The bird is the word'
