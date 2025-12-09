class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, node, key):
        # 1. Standard BST Insert
        if not node:
            return TreeNode(key)
        elif key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        # 2. Update height of ancestor node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # 3. Get balance factor
        balance = self.get_balance(node)

        # 4. If unbalanced, try 4 cases

        # Case 1 - Left Left
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        # Case 2 - Right Right
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        # Case 3 - Left Right
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Case 4 - Right Left
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def pre_order(self, node):
        if not node:
            return
        print(f"{node.key} ", end="")
        self.pre_order(node.left)
        self.pre_order(node.right)

    def in_order(self, node):
        if not node:
            return
        self.in_order(node.left)
        print(f"{node.key} ", end="")
        self.in_order(node.right)

    def post_order(self, node):
        if not node:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(f"{node.key} ", end="")

# Usage
avl = AVLTree()
root = None
keys = [10, 20, 30, 40, 50, 25]

for key in keys:
    root = avl.insert(root, key)

# Preorder traversal to verify structure
print("Preorder traversal of constructed AVL tree is:")
avl.pre_order(root)
# Output should be: 30 20 10 25 40 50

print("\nInorder traversal of constructed AVL tree is:")
avl.in_order(root)

# Output should be: 10 20 25 30 40 50
print("\nPostorder traversal of constructed AVL tree is:")
avl.post_order(root)