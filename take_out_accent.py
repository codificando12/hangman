from get_word import get_the_word

def take_out(word):
    word = word.upper()
    replacements = [
        ["Á", "A"],
        ["É", "E"],
        ["Í", "I"],
        ["Ó", "O"],
        ["Ú", "U"]
    ]

    for a, b in replacements:
        word = word.replace(a, b)
    
    return(word)
if __name__ == "__main__":
    take_out()