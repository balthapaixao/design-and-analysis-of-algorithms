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
