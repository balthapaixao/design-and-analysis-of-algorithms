# Longest Path in Graphs

Na documentação do trabalho, deve-se provar que o problema selecionado pertence à classe NP-completo[3].

Deverão ser implementados pelo menos dois (dois) algoritmos usando diferentes paradigmas entre os estudados na disciplina:

- Força-Bruta (obrigatório)
- Divisão-e-Conquista
- Programação Dinâmica
- Guloso

Deverão ser realizados testes com diferentes instâncias. Entre elas instâncias que ultrapassem (“estourar”) a capacidade de espaço (memória principal) do sistema computacional utilizado. Deve-se também escolher um tempo para se dizer que determinada instância ultrapassou o limite. A escolha desses itens é parte de avaliação do trabalho.

# Descrição do problema

Dado um determinado grafo, esse problema trata de encontrar seu maior comprimento simples. Ou seja, achar a maior sequência de nós consecutivos sem que haja um ciclo [1](https://www.altcademy.com/blog/discover-the-longest-path-in-a-directed-acyclic-graph-solved/#:~:text=The%20longest%20path%20problem%20is,no%20cycles%20in%20the%20graph.).

## NP-hardness

The NP-hardness of the unweighted longest path problem can be shown using a reduction from the Hamiltonian path problem: a graph G has a Hamiltonian path if and only if its longest path has length n − 1, where n is the number of vertices in G. Because the Hamiltonian path problem is NP-complete, this reduction shows that the decision version of the longest path problem is also NP-complete. In this decision problem, the input is a graph G and a number k; the desired output is yes if G contains a path of k or more edges, and no otherwise.[1]

If the longest path problem could be solved in polynomial time, it could be used to solve this decision problem, by finding a longest path and then comparing its length to the number k. Therefore, the longest path problem is NP-hard. The question "does there exist a simple path in a given graph with at least k edges" is NP-complete.[2]

In weighted complete graphs with non-negative edge weights, the weighted longest path problem is the same as the Travelling salesman path problem, because the longest path always includes all vertices.[3]

https://en.wikipedia.org/wiki/Longest_path_problem

# Cenários e aplicações

- Agendamento de tarefas com dependências;
- Encontrar o caminho crítico em rede de gerenciamento de projetos;
- Analizar redes reguladoras de genes em biologia;
-

# Algortimo

Following is complete algorithm for finding longest distances.

Initialize dist[] = {NINF, NINF, ….} and dist[s] = 0 where s is the source vertex. Here NINF means negative infinite.
Create a topological order of all vertices.
Do following for every vertex u in topological order.
..Do following for every adjacent vertex v of u
……if (dist[v] < dist[u] + weight(u, v))
………dist[v] = dist[u] + weight(u, v)
