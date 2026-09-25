import random
def guesser(guess='',number=''):
    if number == '':
         number = random.randrange(1,101)
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
    