class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
            
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recurvise(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value) 

    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
   
    def preoder(self):
        result = []
        self._preoder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postoder(self):
        result = []
        self._postoder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, node, value):
        if node is None:
            return None
        
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
    
            successor = self._min_value_node(node.right)
            node.value =successor.value
            node.right = self._delete_recursive(node.right, successor.value)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def level_order(self):
        result = []
        if not self.root:
            return result

        queue = [self.root]
        while queue:
            node = queue.pop(0)
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result

# Creating the tree and testing it
bst = BinarySearchTree()

# Insert values
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(17)

# Search
print("Search 7:", bst.search(7))     # True
print("Search 8:", bst.search(8))     # False

# Inorder Traversal
print("Inorder Traversal:", bst.inorder())  # [3, 5, 7, 10, 12, 15, 17]

for value in [10, 5, 15, 3, 7, 12, 17]:
    bst.insert(value)

print("Inorder:", bst.inorder())         # [3, 5, 7, 10, 12, 15, 17]
print("Preorder:", bst.preorder())       # [10, 5, 3, 7, 15, 12, 17]
print("Postorder:", bst.postorder())     # [3, 7, 5, 12, 17, 15, 10]
print("Level-order:", bst.level_order()) # [10, 5, 15, 3, 7, 12, 17]

bst.delete(15)
print("After deleting 15:", bst.inorder())  # [3, 5, 7, 10, 12, 17]



