
class Node:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class TrieTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = Node()

            current = current.children[char]

        current.is_end_of_word = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
    

    def print_trie(self):
        def _print_trie(node, prefix):
            if node.is_end_of_word:
                print(prefix)
            for char, child_node in node.children.items():
                _print_trie(child_node, prefix + char)
        _print_trie(self.root, "")



if __name__ == "__main__":
    trie = TrieTree()
    trie.insert("hello")
    trie.insert("hi")
    print(trie.search("hello"))  # True
    print(trie.search("hell"))   # False
    print(trie.starts_with("he")) # True
    print(trie.starts_with("ha")) # False
    trie.insert("hey")
    print(trie.search("hey"))    # True
    print(trie.search("hi"))     # True
    print(trie.search("h"))      # False
    trie.print_trie()  # Prints all words in the trie
    
