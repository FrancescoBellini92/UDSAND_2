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

    if not suffix or not path or path not in os.listdir():
        return []

    def _search_file_system(suffix, path):
        files_found = []
        items = [os.path.join(path, item) for item in os.listdir(path)]
        subfolders = filter(lambda item: os.path.isdir(item), items)
        files = filter(lambda item: os.path.isfile(item), items)

        for file in files:
            if file.endswith(suffix):
                files_found.append(file)

        for folder in subfolders:
            files_found.extend(_search_file_system(suffix, folder))

        return files_found

    return _search_file_system(suffix, path)

if __name__ == '__main__':

    # test case 1 -> folder with subfolders and target files
    files = find_files('.c', 'testdir_1')
    print('files found are:', files) # expect ['testdir_1\\t1.c', 'testdir_1\\subdir1\\a.c', 'testdir_1\\subdir3\\subsubdir1\\b.c', 'testdir_1\\subdir5\\a.c']
    for file in ['testdir_1\\t1.c', 'testdir_1\\subdir1\\a.c', 'testdir_1\\subdir3\\subsubdir1\\b.c', 'testdir_1\\subdir5\\a.c']:
        assert(file in files)
    # test case 2 -> folder with subfolders and no target files
    files = find_files('.c', 'testdir_2')
    print('files found are:', files) # expect []
    assert(files == [])


    # test case 3 -> non-existent folder
    files = find_files('.c', 'testdir_3')
    print('files found are:', files) # expect []
    assert(files == [])