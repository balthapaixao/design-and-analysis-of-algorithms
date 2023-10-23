import random


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left is None and self.right is None

    def is_full(self):
        return self.left is not None and self.right is not None

    def is_almost_full(self):
        return (
            self.left is not None
            and self.right is None
            or self.left is None
            and self.right is not None
        )


class BinaryTree:
    def __init__(self):
        self.root = None

    def is_strictly_binary(self):
        return self.is_strictly_binary_recursive(self.root)

    def is_strictly_binary_recursive(self, node):
        if node is None:
            return True
        if node.is_leaf():
            return True
        if node.is_full():
            return self.is_strictly_binary_recursive(
                node.left
            ) and self.is_strictly_binary_recursive(node.right)
        return False

    def is_complete(self):
        return self.is_complete_recursive(self.root)

    def is_complete_recursive(self, node):
        if node is None:
            return True
        if node.is_leaf():
            return True
        if node.is_full():
            return self.is_complete_recursive(node.left) and self.is_complete_recursive(
                node.right
            )
        return False

    def is_almost_full(self):
        return self.is_almost_full_recursive(self.root)

    def is_almost_full_recursive(self, node):
        if node is None:
            return True
        if node.is_leaf():
            return True
        if node.is_almost_full():
            return self.is_almost_full_recursive(
                node.left
            ) and self.is_almost_full_recursive(node.right)
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

    def remove(self, value):
        if self.root is None:
            return
        self.remove_recursive(self.root, value)

    def remove_recursive(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self.remove_recursive(node.left, value)
        elif value > node.value:
            node.right = self.remove_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.value = self.find_min(node.right)
                node.right = self.remove_recursive(node.right, node.value)
        return node

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


def test_random_tree() -> None:
    random_tree = BinaryTree()
    for _ in range(10):
        random_tree.insert(random.randint(0, 100))
    random_tree.print_tree()
    print("Strictly Binary: ", random_tree.is_strictly_binary())
    print("Complete: ", random_tree.is_complete())
    print("Almost Complete: ", random_tree.is_almost_full())


def test_complete_tree() -> None:
    complete_tree = BinaryTree()
    complete_tree.insert(5)
    complete_tree.insert(4)
    complete_tree.insert(7)
    complete_tree.insert(2)
    complete_tree.insert(4)
    complete_tree.insert(6)
    complete_tree.insert(8)
    complete_tree.print_tree()
    print("Strictly Binary: ", complete_tree.is_strictly_binary())
    print("Complete: ", complete_tree.is_complete())
    print("Almost Complete: ", complete_tree.is_almost_full())


def generate_almost_full_tree(levels):
    tree = BinaryTree()
    values = list(range(1, 2 ** (levels - 1) + 1))
    for value in values:
        tree.insert(value)
    return tree


def test_almost_full_tree():
    almost_full_tree = generate_almost_full_tree(4)
    almost_full_tree.print_tree()
    print("Strictly Binary: ", almost_full_tree.is_strictly_binary())
    print("Complete: ", almost_full_tree.is_complete())
    print("Almost Complete: ", almost_full_tree.is_almost_full())


if __name__ == "__main__":
    test_random_tree()
    test_complete_tree()
    test_almost_full_tree()
