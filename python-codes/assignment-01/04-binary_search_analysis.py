import time

# Escreva o algoritmo de busca binária (na forma recursiva e não recursiva) e faça a  análise de tempo de execução do pior caso de cada algoritmo.


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
    binary_search_recursive(elems, 999999)
