# Grafo e Algoritmos para Encontrar o Caminho Mais Longo

Este documento fornece um código em Python que define um grafo e implementa dois algoritmos para encontrar o caminho mais longo em um grafo. O código inclui um algoritmo de força bruta e um algoritmo guloso.

## Configuração de Timeout e Limites de Memória
O código começa importando bibliotecas necessárias e definindo uma exceção customizada TimeoutMemoryError para tratar erros de timeout e memória.

```python
from collections import defaultdict
import functools
import signal
import time
import resource

class TimeoutMemoryError(Exception):
    pass

def timeout_memory_handler(signum, frame):
    raise TimeoutMemoryError("Function execution timed out due to memory limit")

def timer_and_memory(timeout_seconds, memory_limit_mb):
    def decorator(func):
        @functools.wraps(func)
        def wrapper_timer_and_memory(*args, **kwargs):
            ...

```
Em seguida, há um decorator timer_and_memory que envolve funções para configurar timeouts e limites de memória.

## Classe Graph

A classe Graph é responsável por representar um grafo e inclui métodos para adicionar arestas, imprimir o grafo, criar um grafo aleatório e ler um grafo de um arquivo.

```python
from collections import defaultdict
import random

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.V = 0
        self.E = 0

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


## Algoritmos para Encontrar o Caminho Mais Longo

### Brute Force para o Caminho Mais Longo

O método brute_force_lgp implementa um algoritmo de força bruta para encontrar o caminho mais longo no grafo.

```python
def get_all_paths(self, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]

    paths = []
    for neighbor in self.graph[start]:
        if neighbor not in path:
            new_paths = self.get_all_paths(neighbor, end, path)
            paths.extend(new_paths)

    return paths

@timer_and_memory(1200, 10240)
def brute_force_longest_path(self):
    # Encontra o caminho mais longo usando força bruta
    max_path_length = 0
    max_path = []

    for start_node in self.graph:
        for end_node in self.graph:
            if start_node != end_node:
                paths = self.get_all_paths(start_node, end_node)
                for path in paths:
                    path_length = len(path)
                    if path_length > max_path_length:
                        max_path_length = path_length
                        max_path = path

    print("Longest path Brute Force:", max_path)
    print("Length:", max_path_length)

    return max_path

```
#### Detalhes do Método
##### Dupla Iteração sobre Nós
O método utiliza dois loops for para iterar sobre todos os pares possíveis de nós no grafo:
```python
for start_node in self.graph:
    for end_node in self.graph:
        if start_node != end_node:
```
Estes loops consideram todas as combinações únicas de nós no grafo, garantindo que o nó inicial seja diferente do nó final.
##### Geração de Todos os Caminhos
Para cada par de nós, a função get_all_paths é chamada para gerar todos os caminhos possíveis entre esses dois nós:
```python
paths = self.get_all_paths(start_node, end_node)
```
A função get_all_paths utiliza uma abordagem recursiva para encontrar todos os caminhos entre os nós start_node e end_node no grafo.

##### Atualização do Caminho Mais Longo
Para cada caminho gerado, a função verifica o comprimento do caminho e o compara com o caminho mais longo encontrado até agora:

```python
for path in paths:
    path_length = len(path)
    if path_length > max_path_length:
        max_path_length = path_length
        max_path = path
```

### Método greedy_lgp
Este método implementa um algoritmo guloso para encontrar o caminho mais longo em um grafo, utilizando o grau dos nós como critério de escolha.

```python
@timer_and_memory(1200, 10240)
def greedy_lgp(self):
    # Encontra o caminho mais longo usando um algoritmo guloso
    max_path_length = 0
    max_path = []

    for start_node in self.graph:
        current_node = start_node
        path = [current_node]

        while True:
            neighbors = self.graph[current_node]
            if not neighbors:
                break

            # Passo guloso: seleciona o vizinho com o maior grau
            next_node = max(neighbors, key=lambda node: len(self.graph[node]))

            if next_node in path:
                neighbors.remove(next_node)
                if not neighbors:
                    break
                next_node = max(neighbors, key=lambda node: len(self.graph[node]))

            if next_node in path:
                break

            path.append(next_node)
            current_node = next_node

        path_length = len(path)
        if path_length > max_path_length:
            max_path_length = path_length
            max_path = path

    print("Longest path Greedy Algorithm:", max_path)
    print("Length:", max_path_length)

    return max_path
```

#### Detalhes do Método
##### Iteração sobre Nós Iniciais
O método utiliza um loop for para iterar sobre todos os nós iniciais no grafo:

```python
for start_node in self.graph:
```
Este loop considera cada nó como ponto de partida para o caminho mais longo.


##### Inicialização do Caminho
Para cada nó inicial, o método inicia um caminho com esse nó:

```python
current_node = start_node
path = [current_node]

```
##### Loop Guloso
O método entra em um loop guloso que continua até que não haja mais vizinhos para visitar:
```python
while True:
    neighbors = self.graph[current_node]
    if not neighbors:
        break
```

##### Escolha Gulosa do Próximo Nó
Dentro do loop, o método seleciona o próximo nó a ser visitado de forma gulosa, escolhendo o nó com o maior grau:

```python
next_node = max(neighbors, key=lambda node: len(self.graph[node]))
```

Se o próximo nó já estiver no caminho, ele quebra o fluxo:

``` python
if next_node in path:
    break
```

##### Atualização do Caminho Mais Longo
O método atualiza o caminho mais longo se o caminho atual for mais longo:
```python
path.append(next_node)
current_node = next_node

path_length = len(path)
if path_length > max_path_length:
    max_path_length = path_length
    max_path = path
```
#### Considerações
O algoritmo guloso para encontrar o caminho mais longo escolhe os nós com base em seu grau, buscando maximizar o grau dos nós visitados em cada etapa. No entanto, esta abordagem pode não garantir a solução globalmente ótima, e pode encontrar caminhos subótimos em alguns casos.

# Como executar
Dentro da pasta scripts existe um [Makefile](./scripts/Makefile) e a inicialização pode ser feita usando:

``` bash
    make config
```
Esse comando irá inicializar o virtual environment em python3.10.

Executando o comando:
``` bash
    make run
```
Dessa forma os códigos de benchmarking serão executados