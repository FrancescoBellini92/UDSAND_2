"""
TASK EXPLANATION
The Group class allows for the creation of a hierarchy of users and gruoups, similarly to a n-tree structure.

In this case, the search was implemented with a breadth-first traversal, as it made more sense to me that
a given user was searched in such a way rather than with a depth-first approach

To increase efficiency, a set was used for storing user IDs (which should work as long as they are unique)

Overall, the time complexity is O(n), as we have to visit each node of the tree (each group)

The breadth first search was implemented with a queue and a while loop,returning when the user is found
In case of user belonging to multiple groups, the first group is returned
"""

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = set()

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.add(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


root = Group("root")
root.add_user('root_user')


child_1 = Group("child_1_group")
child_1.add_user('child_1_user')
root.add_group(child_1)

child_2 = Group("child_2_group")
child_2.add_user('child_2_user')
root.add_group(child_2)

sub_child = Group("subchild_group")
sub_child.add_user("sub_child_user")
child_1.add_group(sub_child) # case in which one groups has multiple parents
child_2.add_group(sub_child)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
        user(str): user name/id
        group(class:Group): group to check user membership against
    """

    queue = [group]

    print('\nTraversing groups...')
    while len(queue) > 0:

        group = queue.pop(0)
        print('--- %s ---' %group.name)

        if user in group.users:
            print('*** user <%s> found in group <%s> ***' %(group.name, user))
            return True

        queue.extend(group.get_groups())

    print('*** user <%s> not found ***' %user)
    return False


assert(is_user_in_group('root_user', root))
assert(is_user_in_group('child_1_user', root))
assert(is_user_in_group('sub_child_user', root))
assert(not is_user_in_group('sub_sub_child_user', root))