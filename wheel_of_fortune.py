import random

# 1
#open the words file and generate the word for the game. open file is read only. 
with open('words.txt', 'r') as open_file:   
    words_list = open_file.readlines()

easy_level = [word.upper() for word in words_list if len(word) >= 4 and len(word) <= 6]
normal_level = [word.upper() for word in words_list if len(word) >= 6 and len(word) <= 8]
hard_level = [word.upper() for word in words_list if len(word) >= 8]

def  get_random_word(selected_list):
    word = (random.choice(selected_list))
    return word.upper()
    # return "bubble".upper()


    # SETUP "Game Menu"
# let user pick difficulty at beginning of game. done
# at the start let the user know how many letters the word contains - underscores represent characters in word
def setup_game(): 
    print("Let's play a game!\nHow tough are you?!\n\nCan I play, Daddy? (EASY)\nBring 'Em On! (NORMAL)\nI Am Death Incarnate! (HARD)\n")
    # see below for calling of function in "play_game" 
    no_of_guesses = 8
    difficulty = input("Select your fate: ").upper()
    if difficulty == "Can I play, Daddy?" or difficulty == "EASY":
        random_word = get_random_word(easy_level).strip()
        hidden_word = ("_" + " ") * len(random_word)
        print("\nJa, ein... Hot Dog? ")
        print("\nGuesses remaining: ", no_of_guesses)
        print("\n", hidden_word)
    elif difficulty == "Bring 'Em On!" or difficulty == "NORMAL":
        random_word = get_random_word(normal_level).strip()
        hidden_word = ("_" + " ") * len(random_word)
        print("\nEasy now, Johnny Cowboy!")
        print("\nGuesses remaining: ", no_of_guesses)
        print("\n",hidden_word)
        # hard - only 8+ characters
    elif difficulty == "I Am Death Incarnate!" or difficulty == "HARD":
        random_word = get_random_word(hard_level).strip()
        hidden_word = ("_" + " ") * len(random_word)
        print("\nGoddammit, Blazkowicz! You done messed up now!")
        print("\nGuesses remaining: ", no_of_guesses)
        print("\n", hidden_word)
    else:
        print("\nNo, Really... How tough are you?!")
        # return play_game()
        # repeat list of difficulties

    # remove these - no cheating!
    print("\nCheat Code: ",random_word)

        # 3/4/5
        # let the user know if their guess appears in the word - done
        # after each turn, remind user of turns remaining - done
        # set validation for repeat guesses, try again - done
        # user loses a guess only when guessed incorrectly, if they guess a word correctly, they continue - done
    guessed = False
    guessed_letters = []
    no_of_guesses=8
    # //game ends on completion OR when the amount of guesses run out - game seems to go on forever, fix ending it
    while not guessed and no_of_guesses > 0:
        guess = input("Guess a letter fool: ").upper()
        # user supplies one letter (guess) per round, 
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already tried the letter,", guess, "!")
            elif guess not in random_word:
                print(guess, "is not in this word!")
                no_of_guesses -= 1
                print("Guesses Remaining: ", no_of_guesses)
                guessed_letters.append(guess)
            else:
                # //display the partially guessed word, as letters in the word are guessed correctly - still wrapping my head around this one. 
                print("Nice work! Keep on truckin'")
                print("\nGuesses Remaining: ", no_of_guesses)
                guessed_letters.append(guess)
                hidden_word_as_list = list(hidden_word)
                for i in range(len(random_word)):
                    if guess == random_word[i]:
                        hidden_word_as_list[2*i] = guess
                    hidden_word = "".join(hidden_word_as_list)
                    if "_" not in hidden_word:
                        guessed = True
        else:
            # set validation on input - only one letter, let them try again
            print("\nAn error has occurred but the error message cannot be retrieved due to another error. ")
        print("\n", hidden_word)
        print("\n")
    if guessed:
            print("You Win!")
    else:
        print("You Lose!")

# ask if they want to play again - commented out for now until i can get game running in function
def play_game():
    setup_game()
    while input("Do you wanna play again? (Y/N) ").upper() == "Y":
        setup_game()
if __name__ == "__main__":
    play_game()
    
    
    #  HARD STUFF
    # Evil version of the game
