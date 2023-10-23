class DoubleStack:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size
        self.top1 = -1
        self.top2 = size

    def push1(self, element):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.array[self.top1] = element
        else:
            print("Stack Overflow")
            exit(1)

    def push2(self, element):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.array[self.top2] = element
        else:
            print("Stack Overflow")
            exit(1)

    def pop1(self):
        if self.top1 >= 0:
            element = self.array[self.top1]
            self.top1 -= 1
            return element
        else:
            print("Stack Underflow")
            exit(1)

    def pop2(self):
        if self.top2 < self.size:
            element = self.array[self.top2]
            self.top2 += 1
            return element
        else:
            print("Stack Underflow")
            exit(1)

    def print_stack(self):
        print("Stack 1: ", end="")
        for i in range(0, self.top1 + 1):
            print(self.array[i], end=" ")
        print()
        print("Stack 2: ", end="")
        for i in range(self.size - 1, self.top2 - 1, -1):
            print(self.array[i], end=" ")
        print()


import random


def test_stack_overflow():
    double_stack = DoubleStack(5)
    for _ in range(5):
        double_stack.push1(random.randint(0, 100))
        double_stack.push2(random.randint(0, 100))
        double_stack.print_stack()


def test_stack_underflow():
    double_stack = DoubleStack(11)
    for _ in range(5):
        double_stack.push1(random.randint(0, 100))
        double_stack.push2(random.randint(0, 100))
        double_stack.print_stack()
    double_stack.print_stack()
    double_stack.pop1()
    double_stack.pop1()
    double_stack.pop1()
    double_stack.pop1()
    double_stack.pop1()
    double_stack.pop1()
    double_stack.print_stack()


def test_stack():
    double_stack = DoubleStack(10)
    for _ in range(5):
        double_stack.push1(random.randint(0, 100))
        double_stack.push2(random.randint(0, 100))
        double_stack.print_stack()
    double_stack.print_stack()


def test():
    try:
        test_stack()
        print()
    except:
        print()

    try:
        test_stack_underflow()
    except:
        print()

    try:
        test_stack_overflow()
    except:
        print()


if __name__ == "__main__":
    test()
