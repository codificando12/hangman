import random


def read():
    words = []
    with open("./file/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line)
    hola = random.randint(0, len(words))
    word = words[hola]
    print(word)
def run():
    read()


if __name__ == "__main__":
    run()