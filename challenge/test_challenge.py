import unittest
from challenge import guesser

class Test_Number_Guesser():

    def test_exists(self,):
        guesser(1,2)

    def test_returns(self):
         guesser(2,1) == ''

    def test_guesser_takes_input(self):
        guesser(2,3)

    def test_guesser_generates_number(self):
        guesser(1)

    def test_returns_higher(self):
        guesser(0,50) == 'The Number is Higher'

    def test_returns_lower(self):
        guesser(200,50) == 'The Number is Lower'

    def test_set_number_and_guess(self):
        guesser(50,76)

    def test_guess_is_correct(self):
        guesser(50,50) == 'Correct!'

    def test_string_is_correct(self):
            guesser('50',50) == 'Correct!'

    def test_decimal(self):
        guesser(10.5,10) == 'Please Enter an Integer!'

    def test_string(self):
        guesser('asdf',50) == 'Please Enter an Integer!'

    

if __name__=='__main__':
    unittest.main()