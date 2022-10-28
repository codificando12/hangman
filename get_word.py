import random

def get_the_word():
    words = []
    with open("./file/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line)
    choosing = random.randint(0, len(words))
    word = words[choosing]
    return word.upper()