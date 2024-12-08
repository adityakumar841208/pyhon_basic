from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)

        return root

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.key, end=" ")
            self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.key, end=" ")

    def levelorder_traversal(self, root):
        if root is None:
            return
        
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            print(node.key, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

# Create the tree and insert nodes
tree = Tree()
tree.root = tree.insert(tree.root, 3)
tree.root = tree.insert(tree.root, 5)
tree.root = tree.insert(tree.root, 2)
tree.root = tree.insert(tree.root, 7)
tree.root = tree.insert(tree.root, 6)

# In-order Traversal (Recursive)
print("In-order Traversal:")
tree.inorder_traversal(tree.root)
print()

# Pre-order Traversal (Recursive)
print("Pre-order Traversal:")
tree.preorder_traversal(tree.root)
print()

# Post-order Traversal (Recursive)
print("Post-order Traversal:")
tree.postorder_traversal(tree.root)
print()

# Level-order Traversal (Using Queue)
print("Level-order Traversal:")
tree.levelorder_traversal(tree.root)
print()
