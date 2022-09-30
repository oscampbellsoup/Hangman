# Random for selection of chosen word; hangman_words for list of words
import random
import hangman_art
# Set variables
end_of_game = False
right_guess = False
new_word_list = hangman_art.word_list
new_logo = hangman_art.logo
new_stages = hangman_art.stages
chosen_word = random.choice(new_word_list)
word_length = len(chosen_word)
lives = 6
display = []
guess_list = []
# For loop to create unknown word display
for _ in range(word_length):
    display += "_"
print(new_logo)
print(*display)
# While loop to ask input until game is over
while not end_of_game:
    guess = input("Guess a letter: ").lower()
# Check if guess is in any letter of the word    
    for position in range(word_length):
        letter = chosen_word[position]
# If guess is correct, letter will be added to display        
        if letter == guess:
            display[position] = letter
            right_guess = True
    print(*display)
# If right_guess is not True, live will be taken, stage will be shown
    if right_guess == False:  
        lives -= 1
        print(new_stages[lives])
        print(f"The letter {guess} is not in the word.")
# If player loses all lives, game is ended in win    
    if lives == 0:
        end_of_game = True
        print("You lose.")
        print(f"The word is {chosen_word}")
# If player guesses entire word, game is ended in win  
    if "_" not in display:
        end_of_game = True
        print("You win.")
# UI: If player guesses a letter more than once, they will be notified
    if guess in guess_list:
        print(f"You have already guessed the letter, {guess}.")
# guess_list will identify guesses beforehand and add guesses if new
    guess_list += guess
# right_guess changed to false at end of loop if made correct guess before
    right_guess = False