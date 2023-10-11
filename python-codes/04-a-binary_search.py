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
