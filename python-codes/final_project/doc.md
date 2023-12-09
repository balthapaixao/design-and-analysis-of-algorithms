# Grafo e Algoritmos para Encontrar o Caminho Mais Longo

Este documento fornece um código em Python que define um grafo e implementa dois algoritmos para encontrar o caminho mais longo em um grafo. O código inclui um algoritmo de força bruta e um algoritmo guloso.

## Definindo a Classe Graph

A classe Graph é responsável por representar um grafo e inclui métodos para adicionar arestas, imprimir o grafo, criar um grafo aleatório e ler um grafo de um arquivo.

```python
from collections import defaultdict
import random

class Graph:
def **init**(self):
self.graph = defaultdict(list)
self.V = 0 # Número de nós
self.E = 0 # Número de arestas

    def __iter__(self):
        for node in self.graph:
            yield node

    def add_edge(self, u, v):
        # Adiciona uma aresta ao grafo
        # ...

    def print_graph(self):
        # Imprime o grafo
        # ...

    def create_random_graph(self, nodes: int = 20):
        # Cria um grafo aleatório com o número especificado de nós
        # ...

    def read_from_file(self, file_name):
        # Lê um grafo de um arquivo
        # ...
```

## Algoritmo de Força Bruta

O método brute_force_lgp implementa um algoritmo de força bruta para encontrar o caminho mais longo no grafo.

```python
@timer_and_memory(1200, 10240)
def brute_force_lgp(self): # Encontra o caminho mais longo usando força bruta # ...
```

1. **Inicialização:**

   - Inicializa variáveis max_length e max_path para armazenar o comprimento máximo e o caminho máximo encontrado.
   - Define a função interna dfs (Depth-First Search) que realiza a busca em profundidade para encontrar o caminho mais longo a partir de um nó dado.

2. **Iteração pelos Nós do Grafo:**

   - Itera sobre todos os nós no grafo usando um loop for.
   - Para cada nó de início, inicia uma busca em profundidade (dfs) para encontrar o caminho mais longo a partir desse nó.

Busca em Profundidade (dfs):

A função dfs é uma busca em profundidade recursiva que explora todos os caminhos possíveis a partir de um nó.
Mantém o controle do caminho atual, seu comprimento e os nós visitados.
Atualiza max_length e max_path se um caminho mais longo é encontrado.
Saída:

Imprime o caminho mais longo e seu comprimento no final da execução.
Retorna o comprimento do caminho mais longo.

## Algoritmo Guloso

O método greedy_lgp implementa um algoritmo guloso para encontrar o caminho mais longo no grafo.

```python
@timer_and_memory(1200, 10240)
def greedy_lgp(self): # Encontra o caminho mais longo usando algoritmo guloso # ...
```

O código usa um decorador timer_and_memory para controlar o tempo de execução e o limite de memória dos algoritmos.

**Observações Importantes:**

- Os métodos add_edge, print_graph, create_random_graph e read_from_file têm implementações específicas que não estão incluídas aqui. Implemente conforme necessário.
- O código faz uso de algumas funções e módulos que não foram fornecidos no trecho de código. Certifique-se de ter esses elementos em seu ambiente de execução.
- Este é um guia básico do código. Certifique-se de adaptar e implementar as funções ausentes e testar o código em seu ambiente de desenvolvimento.
