# Python program to demonstrate insert operation in binary search tree

# A utility class that represents an individual node in a BST


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A utility function to insert a new node with the given key
def insert(root, key):
    if root is None:
        root = Node(key)
    else:
        if key > root.val:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def find_less_eq_n(root, key):
    if root is None:
        return -1

    if root.val == key:
        return key

    if key > root.val:
        k = find_less_eq_n(root.right, key)
        if k == -1:
            return root.val
        else:
            return k

    elif key < root.val:
        return find_less_eq_n(root.left, key)


# A utility function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


# A utility function to do inorder tree traversal
def preorder(root):
    if root:
        print(root.val)
        inorder(root.left)
        inorder(root.right)


# A utility function to do inorder tree traversal
def postorder(root):
    if root:
        inorder(root.left)
        inorder(root.right)
        print(root.val)


# Driver program to test the above functions
# Let us create the following BST
#	 50
# /	 \
# 30	 70
# / \ / \
# 20 40 60 80
# r = Node(50)
# insert(r, Node(30))
# insert(r, Node(20))
# insert(r, Node(40))
# insert(r, Node(70))
# insert(r, Node(60))
# insert(r, Node(80))
#
# # Print inoder traversal of the BST
# inorder(r)


root = None
root = insert(root, 25)
insert(root, 2)
insert(root, 1)
insert(root, 3)
insert(root, 12)
insert(root, 9)
insert(root, 21)
insert(root, 19)
# inorder(root)

result = find_less_eq_n(root, 4)
print(result)
