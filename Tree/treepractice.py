class CreateNode:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.key = key


class Tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, root, key):
        if root is None:
            return CreateNode(key)
        
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)  # Traverse left subtree
            print(root.key)  # Print current node's key
            self.inorder(root.right)  # Traverse right subtree


# Example usage:
a = [4, 2, 5, 7, 1]

tree = Tree()

# Insert nodes into the tree
for data in a:
    tree.root = tree.insert(tree.root, data)

# Print the inorder traversal
tree.inorder(tree.root)
