
def func():
    secret_word = 'bablu'
    guess = ""
    guess_count = 0
    guess_limit = 3
    out_of_guess = False

    while secret_word != guess and not (out_of_guess):
        if guess_count < guess_limit:
            guess = input("enter a guessing word: ")
            guess_count +=1
        else:
            out_of_guess = True
    if out_of_guess:
        print("out of gueses , you lose the game!!!")
    else:
        print("you won the game !!!! congratulations...")
func()
