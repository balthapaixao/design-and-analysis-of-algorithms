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
