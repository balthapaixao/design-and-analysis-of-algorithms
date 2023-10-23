class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left is None and self.right is None

    def is_full(self):
        return self.left is not None and self.right is not None


class BinaryTree:
    def __init__(self):
        self.root = None

    def is_similar(self, tree):
        return self.is_similar_recursive(self.root, tree.root)

    def is_similar_recursive(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is not None and node2 is not None:
            return self.is_similar_recursive(
                node1.left, node2.left
            ) and self.is_similar_recursive(node1.right, node2.right)
        return False

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_recursive(self.root, value)

    def insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert_recursive(node.right, value)

    def print_tree(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self.root

        if node is not None:
            print(" " * (level * 4) + prefix + str(node.value))
            if node.is_full():
                self.print_tree(node.left, level + 1, "L--- ")
                self.print_tree(node.right, level + 1, "R--- ")
            elif node.left is not None:
                self.print_tree(node.left, level + 1, "L--- ")
            elif node.right is not None:
                self.print_tree(node.right, level + 1, "R--- ")


def test_is_similar():
    tree1 = BinaryTree()
    tree1.insert(3)
    tree1.insert(1)
    tree1.insert(2)
    tree1.insert(4)
    tree1.insert(5)
    tree1.print_tree()

    tree2 = BinaryTree()
    tree2.insert(5)
    tree2.insert(2)
    tree2.insert(3)
    tree2.insert(7)
    tree2.insert(8)
    tree2.print_tree()

    if tree1.is_similar(tree2):
        print("Tree 1 and Tree 2 are similar")
    else:
        print("Tree 1 and Tree 2 are not similar")


def test_is_not_similar():
    tree1 = BinaryTree()
    tree1.insert(3)
    tree1.insert(1)
    tree1.insert(2)
    tree1.insert(4)
    tree1.insert(5)
    tree1.print_tree()

    tree2 = BinaryTree()
    tree2.insert(5)
    tree2.insert(8)
    tree2.insert(3)
    tree2.insert(2)
    tree2.insert(7)
    tree2.print_tree()

    if tree1.is_similar(tree2):
        print("Tree 1 and Tree 2 are similar")
    else:
        print("Tree 1 and Tree 2 are not similar")


if __name__ == "__main__":
    test_is_similar()
    print()
    test_is_not_similar()
