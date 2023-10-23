# Relatório de Análise e Projeto de Algoritmos - Lista 01

## Aluno - Balthazar Paixão

### Temas:

    - Listas
    - Pilhas
    - Filas
    - Recursão
    - Complexidade de Algoritmos
    - Árvores Binárias

## Exercício 1

Escreva um programa que apresente os n primeiros números primos a partir do número 1 para um valor n>0 fornecido pelo usuário.

```python
def get_n_primes(n: int) -> list:
    """Returns a list of the first n prime numbers."""
    primes = []
    while len(primes) < n:
        is_prime = False
        prime = primes[-1] + 1 if primes else 2

        while not is_prime:
            for i in range(2, prime):
                if prime % i == 0:
                    prime += 1
                    break
            else:
                is_prime = True
                primes.append(prime)
    return primes


if __name__ == "__main__":
    print(get_n_primes(1))
```

## Exercício 2

Faça um programa que leia um texto do usuário e conte o número de vogais que aparecem. O texto fornecido deve estar em um arquivo.

```python
def read_vowels() -> None:
    txt = input("Digite o texto a ser lido: ")

    vowels = ["a", "e", "i", "o", "u"]

    count_vowels = 0

    for letter in txt:
        if letter in vowels:
            count_vowels += 1
        else:
            continue

    print(f"Total count of vowels is {count_vowels}")


if __name__ == "__main__":
    read_vowels()
```

## Exercício 3

Escrever uma função (e um programa que execute tal função) que determine se uma matriz quadrada de dimensão n(n<100) é uma matriz de permutação. Uma matriz quadrada é chamada de matriz de permutação se seus elementos são apenas 0’s e 1’s e se em cada linha e coluna da matriz existe apena um único valor 1.

```python
import numpy as np


def is_permutation_matrix(matrix: np.array) -> None:
    """Constraints matrix nxn - n < 100"""
    dim = len(matrix)
    one_col_counts = np.zeros(dim)
    one_row_counts = np.zeros(dim)
    for i in range(dim):
        for j in range(dim):
            if (matrix[i, j] > 1) or (matrix[i, j] < 0):
                break
            elif matrix[i, j] == 1:
                one_row_counts[i] += 1
                one_col_counts[j] += 1
            else:
                continue
    if (one_col_counts == one_row_counts).all():
        print("Is permutation matrix")
    else:
        print("Is not permutation matrix")


if __name__ == "__main__":
    matrix = np.array([[0, 3, 1, 0], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
    is_permutation_matrix(matrix=matrix)
```

## Exercício 4

Escreva o algoritmo de busca binária (na forma recursiva e não recursiva) e faça a análise de tempo de execução do pior caso de cada algoritmo.

### a) Sem recursão

```python
import time


def binary_search_non_recursive(elems: list, value: int):
    """Given an ordered list named elems"""
    start_time = time.time()
    start = 0
    end = len(elems)
    while start <= end:
        mid = int((start + end) // 2)

        actual = elems[mid]

        if actual == value:
            break
        elif actual < value:
            start = mid + 1
        else:
            end = mid - 1

    end_time = time.time()
    print(mid)
    print(f"Time elapsed: {end_time - start_time}")


if __name__ == "__main__":
    elems = list(range(1000000))
    binary_search_non_recursive(elems, 999999)
```

### b) Com recursão

```python
import time


def binary_search_recursive(elems: list, value: int):
    """Given an ordered list named elems"""
    start_time = time.time()
    start = 0
    end = len(elems)
    mid = int((start + end) // 2)

    actual = elems[mid]

    if actual == value:
        end_time = time.time()
        print(actual)
        print(f"Time elapsed: {end_time - start_time}")
    elif actual < value:
        binary_search_recursive(elems[mid + 1 :], value)
    else:
        binary_search_recursive(elems[: mid - 1], value)


if __name__ == "__main__":
    elems = list(range(1000000))
    binary_search_recursive(elems, 500000)
```

## Exercício 5

Explique por que a declaração “O tempo de execução do algoritmo A é no mínimo
O(n^2) ” não tem significado.

```python
"""
O tempo de execução de um algoritmo é dado pela função T(n) = O(f(n)), onde f(n) é uma função que depende do tamanho da entrada n. O(n^2) é uma classe de funções, não uma função em si. Portanto, não faz sentido dizer que o tempo de execução de um algoritmo é no mínimo O(n^2).
"""
```

## Exercício 6

Indique para cada par de expressões (A, B) se A é O, o, Ω,Θ e ω de B. Considere:
a) (n^3, nlogn)
b) (nlogn, n^logn)
c) (logn^k, n^logn)

```python
"""
a) n^3 é O(nlogn) e nlogn é Ω(n^3)
b) nlogn é O(n^logn) e n^logn é Ω(nlogn)
c) logn^k é O(n^logn) e n^logn é Ω(logn^k)
"""
```

## Exercício 7

Escreva uma função para trocar os elementos m e n de uma lista simplesmente encadeada (m e n podem ser chaves ou mesmo ponteiros para os elementos – a escolha é sua).

```python

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
        node = self.head

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

    def switch(self, m: int, n: int) -> NodeList:
        """Switches the position of two nodes in the linked list"""

        prev_m = None
        prev_n = None
        actual_m = self.head
        actual_n = self.head

        while actual_m and actual_m.value != m:
            prev_m = actual_m
            actual_m = actual_m.next

        while actual_n and actual_n.value != n:
            prev_n = actual_n
            actual_n = actual_n.next

        if actual_m and actual_n:
            if prev_m:
                prev_m.next = actual_n
            else:
                self.head = actual_n

            if prev_n:
                prev_n.next = actual_m
            else:
                self.head = actual_n

            temp = actual_m.next
            actual_m.next = actual_n.next
            actual_n.next = temp

if __name__ == "__main__":
values_to_add = list(range(10))
random.shuffle(values_to_add)
m, n = random.sample(values_to_add, 2)
print(f"m: {m}, n: {n}")
LinkedList = LinkedList()

    for value in values_to_add:
        LinkedList.insert(value)

    LinkedList.print()
    LinkedList.switch(m, n)
    LinkedList.print()
```

## Exercício 8

Escreva uma função void MoveMenor(TipoLista Lista) que, dada uma lista com um número qualquer de elementos, acha o menor elemento da lista e o move para o começo da lista, como exemplificado na figura abaixo. (Obs. Não vale trocar apenas os campos item ou usar uma lista / fila / pilha auxiliar! Você deverá fazer a manipulação dos apontadores para trocar as células de posição).

```python
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

    def move_smaller(self):
        """Moves the smallest number to the head of the linked list"""

        prev = None
        smallest = self.head
        current = self.head.next

        while current:
            if current.value < smallest.value:
                smallest = current
            current = current.next

        if smallest != self.head:
            prev = self.head
            while prev.next != smallest:
                prev = prev.next

            prev.next = smallest.next
            smallest.next = self.head
            self.head = smallest


if __name__ == "__main__":
    values_to_add = list(range(10))
    random.shuffle(values_to_add)
    LinkedList = LinkedList()

    for value in values_to_add:
        LinkedList.insert(value)

    LinkedList.print()
    LinkedList.move_smaller()
    LinkedList.print()
```

## Exercício 10

Escreva um procedimento não recursivo, com tempo de execução Θ(n) que inverta uma lista simplesmente encadeada de n elementos. Além do custo de armazenar os n elementos, o procedimento não deve gastar mais do que O(1) para inverter a lista.

```python
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
```

## Exercício 11

Desenvolva um método para manter duas pilhas dentro de um único vetor linear (um arranjo) de modo que nenhuma das pilhas incorra em estouro até que toda a memória seja usada, e toda uma pilha nunca seja deslocada para outro local dentro do vetor.

## Exercício 12

Faça um programa para simular um controlador de voo de um aeroporto. Neste programa o usuário deve ser capaz de realizar as seguintes tarefas:

- Listar o número de aviões esperando para decolar;
- Autorizar a decolagem do primeiro avião na fila;
- Adicionar um avião na fila de espera;
- Listar todos os aviões que estão na lista de espera;
- Listar as características do primeiro avião da fila;

Considere que uma estrutura de dados do tipo fila seja usada para manipular os dados e que cada avião possui um nome, um identificador, uma origem e um destino. Se quiser coloque mais informações, nº de passageiros, capacidade, modelo, etc.

## Exercício 13

Quantos antecedentes tem um nó no nível n em uma árvore binária? Prove sua resposta.

## Exercício 14

Implemente um algoritmo que determine se uma árvore binária é:
(a) estritamente binária;
(b) completa;
(c) quase completa

## Exercício 15

Duas árvores binárias são similares se elas são vazias ou se elas não são vazias e suas subárvores da esquerda são similares e suas subárvores da direita são também similares. Escreva um programa para determinar se duas árvores binárias são similares
