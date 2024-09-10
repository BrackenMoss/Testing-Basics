# FizzBuzz
# Write a program that returns the numbers from 1 to 100 in a list. 
# For multiples of 3, return "Fizz" instead of the number, and for multiples of 5, return "Buzz."
# For numbers that are multiples of both 3 and 5, return "FizzBuzz."


def fizzbuzz(input_number):
    return_array = []
    for i in range(1, input_number+1):
        if i % 3 == 0:
            return_array += ['Fizz']
        elif i % 5 == 0:
            return_array += ['Buzz']
        else:
            return_array += [i]

    return return_array

