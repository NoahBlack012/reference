class Tree:
    def __init__(self, root):
        self.root = root

    # O(log n)
    def search(self, search_value, node):
        if node is None:
            return None
        if node.value == search_value:
            return node

        # Search value less than current node - search left node
        if search_value < node.value:
            return self.search(search_value, node.left)

        # Search value greater than current node - search right node
        return self.search(search_value, node.right)

    # O(n)
    def insert(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self.insert(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self.insert(value, node.right)

    def delete(self, value, node):
        if node is None:
            return None

        if value < node.value:
            node.left = delete(value, node.left)
            return node

        if value > node.value:
            node.right = delete(value, node.right)
            return node

        if value == node.value:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.right = self.lift(node.right, node)
                return node

    def lift(self, node, node_to_delete):
        if node.left:
            node.left = self.lift(node.left, node_to_delete)
            return node
        else:
            node_to_delete.value = node.value
            return node.right

    def display(self, node, level=0):
        if node != None:
            self.display(node.left, level + 1)
            print(' ' * 4 * level + '->', node.value)
            self.display(node.right, level + 1)

    def print_tree(self):
        self.display(self.root)

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


tree = Tree(TreeNode(5))

inp = [4, 7, 6, 8, 3, 11, 34, 43, 5]
for i in inp:
    tree.insert(i, tree.root)

tree.print_tree()
tree.delete(5, tree.root)
tree.print_tree()
