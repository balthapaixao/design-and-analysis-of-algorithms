import random


class NodeList:
    """Class that represents a node in a linked list"""

    def __init__(self, value: int, next: "NodeList" = None):
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return f"NodeList({self.value} -> {self.next})"


class LinkedList:
    """Class that represents a linked list"""

    def __init__(self):
        self.head = None

    def __repr__(self) -> str:
        return f"LinkedList({self.head})"

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __len__(self):
        return len(list(iter(self)))

    def print(self):
        for node in self:
            print(node.value, end=" -> ")
        print("None")

    def insert(self, value: int) -> NodeList:
        """Inserts a new node at the beginning of the linked list"""
        node = NodeList(value)
        node.next = self.head
        self.head = node

    def search(self, value: int) -> NodeList:
        """Searches for a node with the given value"""
        node = self.head
        while node and node.value != value:
            node = node.next
        return node

    def delete(self, value: int) -> NodeList:
        if self.head.value == value:
            self.head = self.head.next

        else:
            prev = None
            actual = self.head

            while actual and actual.value != value:
                prev = actual
                actual = actual.next

            if actual:
                prev.next = actual.next
                actual.next = None
                return actual
            else:
                prev.next = None

    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous


if __name__ == "__main__":
    values_to_add = list(range(10))
    random.shuffle(values_to_add)
    LinkedList = LinkedList()

    for value in values_to_add:
        LinkedList.insert(value)

    LinkedList.print()
    LinkedList.reverse()
    LinkedList.print()
