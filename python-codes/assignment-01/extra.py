# transformar duas pilhas em uma fila


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top:
            value = self.top.value
            self.top = self.top.next
            return value
        raise IndexError("The stack is empty")

    def peek(self):
        if self.top:
            return self.top.value
        raise IndexError("The stack is empty")

    def __repr__(self):
        return f"Stack({self.top})"

    def __len__(self):
        return len(list(iter(self)))

    def __iter__(self):
        node = self.top
        while node:
            yield node
            node = node.next

    def print(self):
        for node in self:
            print(node.value, end=" -> ")
        print("None")


class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        self.stack1.push(value)

    def dequeue(self):
        if self.stack2:
            return self.stack2.pop()
        while self.stack1:
            self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def __repr__(self):
        return f"Queue({self.stack1}, {self.stack2})"

    def __len__(self):
        return len(list(iter(self)))

    def __iter__(self):
        node = self.stack1.top
        while node:
            yield node
            node = node.next

        node = self.stack2.top
        while node:
            yield node
            node = node.next

    def print(self):
        for node in self:
            print(node.value, end=" -> ")
        print("None")

    def print_bigO_complexity(self):
        print("Big-O complexity:")
        print("enqueue: O(1)")
        print("dequeue: O(n)")
