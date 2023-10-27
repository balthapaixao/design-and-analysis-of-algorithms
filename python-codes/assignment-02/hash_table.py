def hash_function(key):
    return key % 7


def get_order(letter: str):
    return ord(letter) - 96


def insert(hash_table, word: str):
    for letter in word:
        order = get_order(letter)
        print(order)
        pos = hash_function(order)
        hash_table[pos].append(letter)

    return hash_table


if __name__ == "__main__":
    word = "PESQUISA".lower()
    hash_table = [[], [], [], [], [], [], []]
    hash_table[0].append("a")

    final_hash_table = insert(hash_table, word)
    print(final_hash_table)
