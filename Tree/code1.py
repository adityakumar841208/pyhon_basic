class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    # Insert function
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root
    
    # Delete function
    def delete(self, root, key):
        if root is None:
            return root
        
        # Traverse the tree to find the node to delete
        if key < root.value:
            root.left = self.delete(root.left, key)
        elif key > root.value:
            root.right = self.delete(root.right, key)
        else:
            # Case 1: Node has only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            # Case 2: Node has two children
            root.value = self.min_value_node(root.right).value
            root.right = self.delete(root.right, root.value)
        
        return root
    
    # Helper function to find the minimum value node in the tree
    def min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current
    
    # Inorder traversal (for printing the tree)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value, end=" ")
            self.inorder(root.right)

# Example usage:
bst = BinarySearchTree()
root = None

# Inserting nodes
values = [20, 8, 22, 4, 12, 10, 14]
for value in values:
    root = bst.insert(root, value)

print("Inorder traversal before deletion:")
bst.inorder(root)
print()

# Deleting a node
root = bst.delete(root, 20)
print("Inorder traversal after deleting 20:")
bst.inorder(root)
print()

# Deleting a node with one child
root = bst.delete(root, 8)
print("Inorder traversal after deleting 8:")
bst.inorder(root)
print()

# Deleting a node with two children
root = bst.delete(root, 12)
print("Inorder traversal after deleting 12:")
bst.inorder(root)
