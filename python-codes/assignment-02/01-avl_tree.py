"""
Questão única: 
Faça um programa que leia um arquivo texto (em .txt) e imprima, em ordem alfabética, 
as palavras e a suas frequências no texto, além de indicadores de performance dos 
algoritmos implementados. 
 
A leitura do arquivo deverá desprezar espaços em branco e sinais de pontuação, que 
serão considerados separadores de palavras. Além disso, a leitura deverá converter 
todas as letras maiúsculas em minúsculas. 
 
A  pesquisa  e  inserção  das  palavras  do  texto  deverão  ser  implementadas  com 
as  seguintes estruturas:  
1.  Pesquisa Binária (utilizando um vetor dinâmico para armazenar as palavras). 
2.  Árvore Binária de Pesquisa sem balanceamento. 
3.  Árvore Binária de Pesquisa com balanceamento (Árvore AVL). 
 
Coloque contadores no seu programa para determinar o número de comparações de 
chaves e atribuições dos registros necessários para montar a tabela de frequências 
em cada uma das estruturas acima. Conte apenas o número de comparações para 
montar a estrutura (operações de inserir e pesquisar). Você não deve considerar as 
operações na fase de impressão ordenada. 
 
Calcule também o tempo que cada estrutura leva para montar a tabela. Analise, por 
meio dos dados coletados, a eficiência de cada estrutura. 
 
A entrada de dados será um arquivo de texto contendo um texto qualquer. O arquivo 
texto deverá usar a codificação UTF-8. Seu algoritmo receberá dois parâmetros: (i) 
nome do arquivo texto que deve ser lido e (ii) estrutura a ser utilizada para impressão 
das frequências
"""
import sys
from unidecode import unidecode
import regex as re


def read_input(txt_file: str):
    """
    Read input from a text file and return a list of integers
    """
    with open(txt_file, "r") as f:
        text = f.read()
    decoded_text = clean_text(text)

    return decoded_text


def get_order(letter: str):
    return ord(letter) - 96


def clean_text(text: str):
    decoded_text = unidecode(text).lower()
    decoded_text = re.sub(r"[^\w\s]", "", decoded_text)

    return decoded_text


def get_words(text: str) -> list:
    words = text.split()
    words = sorted(words)

    return words


def preprocess(text_file: str) -> list:
    text = read_input(text_file)
    words = get_words(text)

    return words


def compare_words(word1: str, word2: str) -> int:
    if word1 == word2:
        return 0
    elif word1 > word2:
        return 1
    else:
        return -1


def binary_search(arr, key):
    comparisons = 0
    size = len(arr)
    mid = size // 2

    if size == 0:
        return False, comparisons
    elif arr[mid] == key:
        return True, comparisons
    elif arr[mid] > key:
        comparisons += 1
        return binary_search(arr[:mid], key)
    else:
        comparisons += 1
        return binary_search(arr[mid + 1 :], key)


class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0

    def __repr__(self):
        return f"AVLNode({self.key})"


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        node = AVLNode(key)
        if self.root is None:
            self.root = node
        else:
            self._insert(node, self.root)

    def _insert(self, node, parent):
        if node.key < parent.key:
            if parent.left is None:
                parent.left = node
                node.parent = parent
                self._update_height(node)
            else:
                self._insert(node, parent.left)
        else:
            if parent.right is None:
                parent.right = node
                node.parent = parent
                self._update_height(node)
            else:
                self._insert(node, parent.right)

    def balance(self):
        self._balance(self.root)

    def _balance(self, node):
        if node is None:
            return
        if node.left is None and node.right is None:
            return
        if node.left is None:
            if node.right.height > 0:
                self._rotate_left(node)
        elif node.right is None:
            if node.left.height > 0:
                self._rotate_right(node)
        elif node.left.height - node.right.height > 1:
            self._rotate_right(node)
        elif node.right.height - node.left.height > 1:
            self._rotate_left(node)
        self._balance(node.parent)

    def _rotate_left(self, node):
        right = node.right
        if node.parent is None:
            self.root = right
        elif node.parent.left is node:
            node.parent.left = right
        else:
            node.parent.right = right
        right.parent = node.parent
        node.right = right.left
        if node.right is not None:
            node.right.parent = node
        right.left = node
        node.parent = right
        self._update_height(node)
        self._update_height(right)

    def _rotate_right(self, node):
        left = node.left
        if node.parent is None:
            self.root = left
        elif node.parent.left is node:
            node.parent.left = left
        else:
            node.parent.right = left
        left.parent = node.parent
        node.left = left.right
        if node.left is not None:
            node.left.parent = node
        left.right = node
        node.parent = left
        self._update_height(node)
        self._update_height(left)

    def _update_height(self, node):
        if node is None:
            return
        node.height = (
            max(
                self._get_height(node.left),
                self._get_height(node.right),
            )
            + 1
        )

    def _get_height(self, node):
        if node is None:
            return -1
        return node.height

    def is_balanced(self):
        return self._is_balanced(self.root)

    def _is_balanced(self, node):
        if node is None:
            return True
        if abs(self._get_height(node.left) - self._get_height(node.right)) > 1:
            return False
        return self._is_balanced(node.left) and self._is_balanced(node.right)

    def print_tree(self):
        self._print_tree(self.root)

    def _print_tree(self, node):
        if node is None:
            return
        self._print_tree(node.left)
        print(node.key)
        self._print_tree(node.right)

    def search(self, key):
        return self._search(key, self.root)

    def _search(self, key, node):
        comparisons = 0
        if node is None:
            return False, comparisons
        elif node.key == key:
            return True, comparisons
        elif node.key > key:
            comparisons += 1
            return self._search(key, node.left)
        else:
            comparisons += 1
            return self._search(key, node.right)


def main(key: str):
    txt_file = sys.argv[1]
    method = sys.argv[2]

    if method == "binary_search":
        words = preprocess(txt_file)
        found, comparisons = binary_search(words, "pesquisa")
        if found:
            cnt = words.count(key)
            print(f"Found word {key} {cnt} times with {comparisons} comparisons")
        else:
            print(f"Word {key} not found with {comparisons} comparisons")

    elif method == "avl_tree_unbalanced":
        words = preprocess(txt_file)
        tree = AVLTree()
        for word in words:
            tree.insert(word)
        tree.print_tree()
        print(tree.is_balanced())
        found, comparisons = tree.search(key)
        if found:
            print(f"Found word {key} with {comparisons} comparisons")
        else:
            print(f"Word {key} not found with {comparisons} comparisons")

    elif method == "avl_tree_balanced":
        words = preprocess(txt_file)
        tree = AVLTree()
        for word in words:
            tree.insert(word)
        print(tree.is_balanced())
        tree._balance(tree.root)
        print(tree.is_balanced())
        found, comparisons = tree.search(key)
        if found:
            print(f"Found word {key} with {comparisons} comparisons")
        else:
            print(f"Word {key} not found with {comparisons} comparisons")

    else:
        raise ValueError("Invalid method")


if __name__ == "__main__":
    main("ipsum")
