""" 
- Implemente uma classe Hash respeitando o seguinte: 
a) Utilize uma estrutura de tabela Hash para armazenar os elementos que devem ser 
inseridos e consultados com complexidade O(1).
b) A  estrutura  criada  deve  permitir  o  armazenamento  de  elementos  de  qualquer  tipo. 
Elementos esses identificados por uma chave do tipo string. 

"""


class Hash:
    def __init__(self):
        self.hash_table = {}

    def insert(self, key, value):
        self.hash_table[key] = value

    def search(self, key):
        return self.hash_table[key]

    def delete(self, key):
        del self.hash_table[key]

    def print(self):
        print(self.hash_table)


hash = Hash()
hash.insert("1", "a")
hash.insert("2", "b")
hash.insert("3", "c")
hash.insert("4", "d")
