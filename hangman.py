from get_word import get_the_word
from take_out_accent import take_out


def run():
    word = get_the_word()
    word_without_accent = take_out(word)
    word_completion = "_" * (len(word_without_accent)-1)
    guessed = False
    guessed_letters = []
    guessed_words = []
    life = 6
    print("Vamos a jugar al ahorcado")
    print(f"Tienes {life} vidas")
    print(word_completion)
    print("\n")

    while not guessed and life > 0:
        guess = input("Por favor, escribe una letra o una palabra: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Adivinaste la letra", guess)
            elif guess not in word_without_accent:
                print(f'{guess} no esta en la palabra')
                life -= 1
                guessed_letters.append(guess)
                print(f'Te quedan {life}')
                print(', '.join(guessed_letters))
                
            else:
                print(f'Bien hecho {guess} esta en la palabra')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word_without_accent) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
                    print('Bien hecho! Ganaste')
                    print(word)
                    again = input("¿Quieres jugar de nuevo?(Y/N): ")
                    again = again.upper()
                    if again == "Y":
                        word = get_the_word()
                        word_without_accent = take_out(word)
                        word_completion = "_" * (len(word_without_accent)-1)
                        guessed = False
                        guessed_letters = []
                        guessed_words = []
                        life = 6
                    else:
                        break

        elif len(guess) == len(word_without_accent) and guess.isalpha():
            pass

        else:
            print("Letra incorrecta.")
        print(word_completion)
        if life == 0:
            print(f'La parabara era {word}')
            again = input("¿Quieres jugar de nuevo?(Y/N): ")
            again = again.upper()
            if again == "Y":
                word = get_the_word()
                word_without_accent = take_out(word)
                word_completion = "_" * (len(word_without_accent)-1)
                guessed = False
                guessed_letters = []
                guessed_words = []
                life = 6
            else:
                break


if __name__ == "__main__":
    run()