"""
TASK EXPLANATION
The file system is analogous to a tree, thus an algorithm similar to a depth-first-search can be used

In this case, the search was implemented with a depth-first pre-order traversal

Overall, the time complexity is O(n) as we recursively visit each sub-folder
"""


import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
        suffix(str): suffix if the file name to be found
        path(str): path of the file system

    Returns:
        a list of paths
    """

    files_found = []

    items = [os.path.join(path, item) for item in os.listdir(path)] # 1n
    subfolders = filter(lambda item: os.path.isdir(item), items) # 1n
    files = filter(lambda item: os.path.isfile(item), items) # 1n

    for file in files:
        if file.endswith(suffix):
            files_found.append(file)

    for folder in subfolders:
        files_found.extend(find_files(suffix, folder))

    return files_found

files = find_files('.c', 'testdir')
for file in files:
    print(file)