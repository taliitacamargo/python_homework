# Task 4

def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        word = ""
        for char in secret_word:
            if char in guesses:
                word += char
            else:
                word += "_"
        print(word)
        if "_" in word:
            return False
        else:
            return True

    return hangman_closure


secret_word = input("Enter the secret word: ")
game = make_hangman(secret_word)

done = False
while not done:
    letter = input("Guess a letter: ")
    done = game(letter)

print("You guessed the word!")
