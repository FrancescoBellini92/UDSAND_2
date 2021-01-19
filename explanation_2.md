# TASK 2 EXPLANATION

The file system is analogous to a tree, thus an algorithm similar to a depth-first-search can be used

In this case, the search was implemented with a depth-first pre-order traversal
Considering the n as the number of folders and files, in the worst case each of them is a folder and thus,
given k operations perfomed in a single function call, we would do k * n operations as we recursively visit each sub-folder
Overall, the time complexity is O(n)
