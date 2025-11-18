class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # --- 1. Insert ---
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current, key):
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert_recursive(current.left, key)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert_recursive(current.right, key)

    # --- 2. Search ---
    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current, key):
        if current is None or current.key == key:
            return current
        if key < current.key:
            return self._search_recursive(current.left, key)
        return self._search_recursive(current.right, key)

    # --- 3. Delete ---
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, current, key):
        if current is None:
            return current

        if key < current.key:
            current.left = self._delete_recursive(current.left, key)
        elif key > current.key:
            current.right = self._delete_recursive(current.right, key)
        else:
            # Node found
            # Case 1: No child or one child
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            # Case 2: Two children
            # Get inorder successor (smallest in right subtree)
            temp = self._min_value_node(current.right)
            current.key = temp.key
            # Delete the successor
            current.right = self._delete_recursive(current.right, temp.key)

        return current

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # --- 4. Traverse: Breadth First (Level Order) ---
    def bfs(self):
        result = []
        if not self.root:
            return result
        
        # Using a standard list as a queue
        queue = [self.root]
        while len(queue) > 0:
            # pop(0) is O(n), but avoids imports
            current = queue.pop(0)
            result.append(current.key)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result

    # --- 4. Traverse: Depth First (In-Order) ---
    def dfs_inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, current, result):
        if current:
            self._inorder_recursive(current.left, result)
            result.append(current.key)
            self._inorder_recursive(current.right, result)


    # --- inOrder ---
    def inorder(self):
        return self.dfs_inorder()
    
    # --- preOrder ---
    def preorder(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, current, result):
        if current:
            result.append(current.key)
            self._preorder_recursive(current.left, result)
            self._preorder_recursive(current.right, result)

    # --- postOrder ---
    def postorder(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, current, result):
        if current:
            self._postorder_recursive(current.left, result)
            self._postorder_recursive(current.right, result)
            result.append(current.key)


    # --- count nodes ---
    def count_nodes(self):
        return self._count_nodes_recursive(self.root)
    
    def _count_nodes_recursive(self, current):
        if current is None:
            return 0
        return 1 + self._count_nodes_recursive(current.left) + self._count_nodes_recursive(current.right)


    # --- count leaf nodes ---
    def count_leaf_nodes(self):
        return self._count_leaf_nodes_recursive(self.root)
    
    def _count_leaf_nodes_recursive(self, current):
        if current is None:
            return 0
        if current.left is None and current.right is None:
            return 1
        return self._count_leaf_nodes_recursive(current.left) + self._count_leaf_nodes_recursive(current.right)
    


def is_trees_identical(node1, node2):
    if node1 is None and node2 is None:
        return True
    if node1 is not None and node2 is not None:
        return (node1.key == node2.key and
                is_trees_identical(node1.left, node2.left) and
                is_trees_identical(node1.right, node2.right))
    return False


def BalencedBST(sorted_array):
    if not sorted_array:
        return None

    mid = len(sorted_array) // 2
    node = Node(sorted_array[mid])
    node.left = BalencedBST(sorted_array[:mid])
    node.right = BalencedBST(sorted_array[mid+1:])
    return node



# --- Usage ---
bst = BinarySearchTree()
for x in [50, 30, 20, 40, 70, 60, 80]:
    bst.insert(x)

print(f"Search 40: {bst.search(40) is not None}")
print(f"BFS: {bst.bfs()}")
bst.delete(50)
print(f"After Delete 50 (DFS): {bst.dfs_inorder()}")
print(f"Preorder: {bst.preorder()}")
print(f"Postorder: {bst.postorder()}")
print(f"Total Nodes: {bst.count_nodes()}")
print(f"Leaf Nodes: {bst.count_leaf_nodes()}")

# Create another BST for comparison
bst2 = BinarySearchTree()
for x in [30, 20, 40, 70, 60, 80]:
        bst2.insert(x)

print(f"Trees identical: {is_trees_identical(bst.root, bst2.root)}")

# Create Balanced BST from sorted array
sorted_array = [10, 20, 30, 40, 50,
                60, 70, 80, 90]
balanced_root = BalencedBST(sorted_array)
balanced_bst = BinarySearchTree()

