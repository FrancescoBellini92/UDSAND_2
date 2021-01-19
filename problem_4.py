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
child_1.add_group(sub_child) # case in which one groups has multiple parents (see test case 3)
child_2.add_group(sub_child)

child_1.add_user('common_child_user') # case in which one user is shared across several groups (see test case 4)
child_2.add_user('common_child_user')


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
            print('*** user <%s> found in group <%s> ***' %(user, group.name))
            #expect that when a user belongs to a group that has multile parents,
            # iteration ends at first occurence

            # expect that for shared users (users belonging to multiple groups)
            # iteration ends when at user first occurrence

            return True

        queue.extend(group.get_groups())

    print('*** user <%s> not found ***' %user)
    return False

# test case 1 -> user is in root group
is_found = is_user_in_group('root_user', root)
print('the user has been found?', is_found) # expect True
assert(is_found)

# test case 2 -> user is in child group
is_found = is_user_in_group('child_1_user', root)
print('the user has been found?', is_found) # expect True
assert(is_found)


# test case 3 -> user is in subgroup that belongs to two parent groups
is_found = is_user_in_group('sub_child_user', root)
print('the user has been found?', is_found) # expect True
assert(is_found)

# test case 4 -> user present in two groups
is_found = is_user_in_group('common_child_user', root)
print('the user has been found?', is_found) # expect False
assert(is_found)

# test case 5 -> user is not present in any group
is_found = is_user_in_group('absent_user', root)
print('the user has been found?', is_found) # expect False
assert(not is_found)
