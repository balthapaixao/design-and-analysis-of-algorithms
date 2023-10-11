def read_vowels() -> None:
    txt = input("Digite o texto a ser lido: ")

    vowels = ["a", "e", "i", "o", "u"]

    count_vowels = 0

    for letter in txt:
        if letter in vowels:
            count_vowels += 1
        else:
            continue

    print(f"Total count of vowels is {count_vowels}")


if __name__ == "__main__":
    read_vowels()
