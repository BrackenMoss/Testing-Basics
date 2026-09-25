import random
def guesser(guess,number):
    try:
          guess = int(guess)
    except:
            return 'Please Enter an Integer!' 
    if guess < number:
        return 'The Number is Higher'
    elif guess > number:
        return 'The Number is Lower'
    elif guess == number:
        return 'Correct!'
    else:
        return 'Please Enter an Integer!' 
    

def guesser_game():
    print("Let's Play a Guessing Game! What Number am I Thinking Of?")
    guess = input()
    number = random.randrange(1,101)
    while True:
        if guesser(guess,number) != 'Correct!':
            print(guesser(guess,number))
            print("Try Again!")
            guess = input()
        elif guesser(guess,number) == 'Correct!':
            print(guesser(guess,number))
            print("Great Job!")
            return True
    

if __name__ == '__main__':
    guesser_game()