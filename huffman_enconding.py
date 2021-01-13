
from data_structures.linked_list.double_linked_list import *
import sys

class TreeNode:

    def __init__(self, value = None):
        self.left = None
        self.right = None
        self.value = value
        self.previous = None
        self.next = None


    def __repr__(self):
        return str(self.value[1])

class HuffmanTree:
    def __init__(self, root):
        self.root = root
        self.prefix_char_map = {}

    def __repr__(self):
        queue = [(self.root, 0)]

        print_queue = []
        while len(queue) > 0:
            node, level = queue.pop(0)
            print(node.value, level)

            if isinstance(node, TreeNode):
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))

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

    def get_prefix_map(self):
        char_prefix_map = {}

        def _traverse(node, prefix_code = ''):
            if isinstance(node, TreeNode):
                if node.left:
                    _traverse(node.left, prefix_code + '0')
                if node.right:
                    _traverse(node.right, prefix_code + '1')
            else:
                char_prefix_map[node.value[0]] = prefix_code
                self.prefix_char_map[prefix_code] = node.value[0]
                print(char_prefix_map)

        _traverse(self.root)

        return char_prefix_map



def huffman_encoding(data):
    frequency_map = {}

    priority_queue = DoublyLinkedList()

    for char in data:
        frequency_map.setdefault(char, 0)
        frequency_map[char] += 1

    for char in frequency_map:
        frequency = frequency_map[char]
        priority_queue.append((char, frequency))

    for node in priority_queue:
        print(node)

    def _create_tree():
        print('\n')
        print(priority_queue.to_list())
        if priority_queue.size() == 1:
            return priority_queue.head

        minimun = 1000
        to_merge = []
        minimun_node = None
        for node in priority_queue:
            frequency = node.value[1]
            if frequency <= minimun:
                minimun = frequency
                minimun_node = node
        to_merge.append(minimun_node)
        priority_queue.remove_node(minimun_node)

        minimun_node = None
        minimun = 1000
        for node in priority_queue:
            frequency = node.value[1]
            if frequency <= minimun:
                minimun = frequency
                minimun_node = node
        to_merge.append(minimun_node)
        priority_queue.remove_node(minimun_node)


        freq_1 = to_merge[0].value[1]
        freq_2 = to_merge[1].value[1]
        merged = TreeNode(('', freq_1 + freq_2))
        merged.left = to_merge[0]
        merged.right = to_merge[1]
        priority_queue.prepend_node(merged)

        return _create_tree()

    tree = HuffmanTree(_create_tree())
    print(tree)
    prefix_map = tree.get_prefix_map()

    encoded = ''
    for char in data:
        encoded = encoded + prefix_map[char]

    return encoded, tree


def huffman_decoding(data,tree):
    decoded = ''
    char_buffer = ''
    for char in data:
        char_buffer = char_buffer + char
        if char_buffer in tree.prefix_char_map:
            decoded = decoded + tree.prefix_char_map[char_buffer]
            char_buffer = ''
    print(decoded)
    return decoded


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))