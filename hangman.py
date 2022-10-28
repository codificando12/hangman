from get_word import get_the_word
from hide_word import hide_the_word


def run():
    word = get_the_word()
    hidding = hide_the_word(word)
    print(hidding)
    print("Let's play Hangman")
    for letter in range(0, len(hidding)):
        if len(hidding) > 0:
            write = input("Write a letter: ")
            write = write.upper()
            if write in hidding:
                print(hidding.index(write))
    print(hidding)        
        
        

if __name__ == "__main__":
    run()