class TwoThreeNode:
    def __init__(self, key):
        self.key1 = key
        self.key2 = None
        self.left = None
        self.middle = None
        self.right = None

    def is_leaf(self):
        return self.left is None and self.middle is None and self.right is None

    def is_full(self):
        return self.key2 is not None

    def has_key(self, key):
        return self.key1 == key or self.key2 == key

    def get_child(self, key):
        if key < self.key1:
            return self.left
        elif self.key2 is None or key < self.key2:
            return self.middle
        else:
            return self.right


class TwoThreeTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TwoThreeNode(key)
        else:
            p_key, p_ref = self._insert(self.root, key)
            if p_key is not None:  # new root created
                newnode = TwoThreeNode(p_key)
                newnode.left = self.root
                newnode.middle = p_ref
                self.root = newnode

    def _insert(self, node, key):
        if node.has_key(key):  # duplicate key
            return None, None
        elif node.is_leaf():  # insert only to leaf node
            return self._add_to_node(node, key, None)
        else:
            child = node.get_child(
                key
            )  # get reference to the child/subtree for further operations
            p_key, p_ref = self._insert(child, key)
            if p_key is None:
                return None, None
            else:
                return self._add_to_node(node, p_key, p_ref)

    def _add_to_node(self, node, key, p_ref):
        if node.is_full():  # insertion into a full node requires split
            return self._split_node(node, key, p_ref)
        else:  # if not full, then insert into the node
            if key < node.key1:
                node.key2 = node.key1
                node.key1 = key
                if p_ref is not None:
                    node.right = node.middle
                    node.middle = p_ref
            else:
                node.key2 = key
                if p_ref is not None:
                    node.right = p_ref
            return None, None

    def _split_node(self, node, key, p_ref):
        newnode = TwoThreeNode(None)
        if key < node.key1:  # key,key1,key2 -> key1 promoted to parent
            p_key = node.key1
            node.key1 = key
            newnode.key1 = node.key2
            if p_ref is not None:
                newnode.left = node.middle
                newnode.middle = node.right
                node.middle = p_ref
        elif key < node.key2:  # key1,key,key2 -> key promoted to parent
            p_key = key
            newnode.key1 = node.key2
            if p_ref is not None:
                newnode.left = p_ref
                newnode.middle = node.right
        else:  # key1,key2,key -> key2 promoted to parent
            p_key = node.key2
            newnode.key1 = key
            if p_ref is not None:
                newnode.left = node.right
                newnode.middle = p_ref
        node.key2 = None  # only 1 key remains
        node.right = None  # update the 2nd child reference in the node, as it contains only 1 key now
        return p_key, newnode

    def traverse_inorder(self, node):
        if node is not None:
            if node.is_leaf():
                print(node.key1, end=" ")
                if node.key2 is not None:
                    print(node.key2, end=" ")
            else:
                self.traverse_inorder(node.left)
                print(node.key1, end=" ")
                self.traverse_inorder(node.middle)
                if node.key2 is not None:
                    print(node.key2, end=" ")
                    self.traverse_inorder(node.right)

    def traverse_preorder(self, node):
        if node is not None:
            print(node.key1, end=" ")
            if node.key2 is not None:
                print(node.key2, end=" ")
            self.traverse_preorder(node.left)
            self.traverse_preorder(node.middle)
            self.traverse_preorder(node.right)

    def traverse_postorder(self, node):
        if node is not None:
            self.traverse_postorder(node.left)
            self.traverse_postorder(node.middle)
            self.traverse_postorder(node.right)
            print(node.key1, end=" ")
            if node.key2 is not None:
                print(node.key2, end=" ")

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if node.has_key(key):
            return True
        if node.is_leaf():
            return False
        child = node.get_child(key)
        return self._search(child, key)

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        if node.is_leaf():
            return 1
        return 1 + self._height(node.left)


if __name__ == "__main__":
    tree = TwoThreeTree()
    keys = [10, 20, 5, 6, 12, 30, 25]
    for key in keys:
        tree.insert(key)

    print("Traversal of 2-3 tree:")
    tree.traverse_inorder(tree.root)
    print()

    search_keys = [6, 15, 25, 55]
    for key in search_keys:
        found = tree.search(key)
        print(f"Key {key} found: {found}")
