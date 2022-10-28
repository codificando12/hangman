from get_word import get_the_word

def hide_the_word(word):
    word = word
    lst = [i for i in word if i != "\n"]
    return lst
if __name__ == "__main__":
    hide_the_word()