import random


from hangman_words_api import get_random_word
from hangman_art import stages, logo


lives = 6


print(logo)
from hangman_words_api import get_random_word

chosen_word = get_random_word()


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:


    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()


    if guess in correct_letters:
        print(f"You have already guessed {guess}")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)



    if guess not in chosen_word:
        lives -= 1
        print( f"You guessed d, that's not in the word. You lose a life." )

        if lives == 0:
            game_over = True

            
            print(f"***********************It was {chosen_word}! YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")


    print(stages[lives])
