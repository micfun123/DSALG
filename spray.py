class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class SplayTree:
    def __init__(self):
        self.root = None

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        
        y.right = x
        x.parent = y

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        
        y.left = x
        x.parent = y

    def _splay(self, n):
        """Moves node n to the root using rotations."""
        while n.parent:
            # Case 1: Parent is root (Zig)
            if not n.parent.parent:
                if n == n.parent.left:
                    self._right_rotate(n.parent)
                else:
                    self._left_rotate(n.parent)
            # Case 2: Zig-Zig (Linear) or Zig-Zag (Bent)
            else:
                p = n.parent
                g = p.parent
                
                # Check orientation
                if n == p.left and p == g.left:     # Zig-Zig
                    self._right_rotate(g)
                    self._right_rotate(p)
                elif n == p.right and p == g.right: # Zag-Zag
                    self._left_rotate(g)
                    self._left_rotate(p)
                elif n == p.right and p == g.left:  # Zig-Zag
                    self._left_rotate(p)
                    self._right_rotate(g)
                else:                               # Zag-Zig
                    self._right_rotate(p)
                    self._left_rotate(g)

    def insert(self, key):
        """Inserts a key and splays it to the root."""
        n = Node(key)
        y = None
        x = self.root

        # Standard BST Insert
        while x:
            y = x
            if n.key < x.key:
                x = x.left
            else:
                x = x.right
        
        n.parent = y
        if not y:
            self.root = n
        elif n.key < y.key:
            y.left = n
        else:
            y.right = n
        
        # Splay the new node to root
        self._splay(n)

    def search(self, key):
        """Searches for a key, splays the found node (or last accessed) to root."""
        x = self.root
        last_accessed = None

        while x:
            if key == x.key:
                self._splay(x)
                return x
            
            last_accessed = x
            if key < x.key:
                x = x.left
            else:
                x = x.right
        
        # If not found, splay the last accessed node (neighbor)
        if last_accessed:
            self._splay(last_accessed)
        return None

    def inorder(self):
        """Helper to print tree structure."""
        def _recurse(node):
            if node:
                _recurse(node.left)
                print(node.key, end=' ')
                _recurse(node.right)
        _recurse(self.root)
        print()

    def preorder(self):
        """Helper to print tree structure in preorder."""
        def _recurse(node):
            if node:
                print(node.key, end=' ')
                _recurse(node.left)
                _recurse(node.right)
        _recurse(self.root)
        print()

    def postorder(self):
        """Helper to print tree structure in postorder."""
        def _recurse(node):
            if node:
                _recurse(node.left)
                _recurse(node.right)
                print(node.key, end=' ')
        _recurse(self.root)
        print()

# Usage Example
if __name__ == "__main__":
    st = SplayTree()
    st.insert(10)
    st.insert(20)
    st.insert(30)
    
    print("Inorder traversal after inserts:")
    st.inorder()
    
    print("Root before search(10):", st.root.key)
    st.search(10)
    print("Root after search(10):", st.root.key)  # 10 should be root now