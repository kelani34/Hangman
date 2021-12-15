import random

from hangman_words import word_list, word_class

from hangman_art import stages, logo

print(logo)

end_of_game = False

chosen_word = random.choice(word_list)

word_length = len(chosen_word)

lives = 26

display = []

for letters in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("choose a random letter:").lower()    

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess} that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(display) 

    if "_" not in display:
        end_of_game = True
        print("Great, You won")

    print(stages[lives])
    









from os import system, name
  

# from time import sleep
  
# def clear():
  
#     if name == 'nt':
#         _ = system('cls')
  
#     # for mac and linux(here, os.name is 'posix')
#     else:
#         _ = system('clear')
  
# # print out some text
# print('hello geeks\n'*10)
  
# # sleep for 2 seconds after printing output
# sleep(2)
  
# # now call function we defined above
# clear()