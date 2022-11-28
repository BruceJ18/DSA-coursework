# --------- Binary Tree, Binary Search Tree, and Balanced Binary Search Tree Code ---------
# create User class to create User instances for elements within user database
class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def introduce_yourself(self, guest_name):
        print(f"Hi {guest_name}, I'm {self.name}! Contact me at {self.email}.")

# user data base for storing, inserting, updating, finding, and listing all users
# BRUTE FORCE METHOD
# time complexity O(log(n))
    class UserDatabase:
        def __init__(self):
            self.users = []

        def insert(self, user):
            i = 0
            while i < len(self.users):
                if self.users[i].username > user.username:
                    break
                i += 1
            self.users.insert(i, user)

        def find(self, username):
            for user in self.users:
                if user.username == username:
                    return user

        def update(self, user):
            target = self.find(user.username)
            target.name, target.email = user.name, user.email

        def list_all(self):
            return self.users



# process of creating binary tree
# create instances with this class and
# connect those instances in a tree-like structure
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

# more convenient tuple that is created
# by using a helper function to "parse a tuple"
# and create a new root node that is of
# the TreeNode class
# This way the TreeNode instance is able to more conveniently
# call a key or lower level tuple elements
tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))

def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode_Updated(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode_Updated(data)
    return node


def display_keys(node, space='\t', level=0):
    # If the node is empty
    if node is None:
        print(space * level + '∅')
        return

        # If the node is a leaf
    if node.left is None and node.right is None:
        print(space * level + str(node.key))
        return

    # If the node has children
    display_keys(node.right, space, level + 1)
    print(space * level + str(node.key))
    display_keys(node.left, space, level + 1)

# in order traversal
def traverse_in_order(node):
    if node is None:
        return []
    return(traverse_in_order(node.left) +
           [node.key] +
           traverse_in_order(node.right))


# pre order traversal
def traverse_pre_order(node):
    if node is None:
        return []
    return ([node.key] + traverse_pre_order(node.left) + traverse_pre_order(node.right))

# encapsulation of all methods defined above from parse tuple
# to in order and pre order traversals
class TreeNode_Updated():
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None

    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode_Updated.height(self.left), TreeNode_Updated.height(self.right))

    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode_Updated.size(self.left) + TreeNode_Updated.size(self.right)

    def traverse_in_order(self):
        if self is None:
            return []
        return (TreeNode_Updated.traverse_in_order(self.left) +
                [self.key] +
                TreeNode_Updated.traverse_in_order(self.right))

    def display_keys(self, space='\t', level=0):
        # If the node is empty
        if self is None:
            print(space * level + '∅')
            return

            # If the node is a leaf
        if self.left is None and self.right is None:
            print(space * level + str(self.key))
            return

        # If the node has children
        display_keys(self.right, space, level + 1)
        print(space * level + str(self.key))
        display_keys(self.left, space, level + 1)

    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode_Updated.to_tuple(self.left), self.key, TreeNode_Updated.to_tuple(self.right)

    @staticmethod
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode_Updated(data[1])
            node.left = TreeNode_Updated.parse_tuple(data[0])
            node.right = TreeNode_Updated.parse_tuple(data[2])
        else:
            node = TreeNode_Updated(data)
        return node


# similar class as TreeNode above
# but
class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None



def make_balance_bst(data, start, end=None, parent=None):
    if end is None:
        end = len(data) - 1
    if start > end:
        return None

    mid = (start + end)/2
    key, value = data[mid]

    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balance_bst(data, start, mid-1, parent)
    root.right = make_balance_bst(data, mid+1, end, parent)

    return root





