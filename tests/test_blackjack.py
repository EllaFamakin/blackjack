from unittest import TestCase, main
from unittest.mock import patch
from test_helper import run_test

class TestBlackjack(TestCase):

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_example(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.

        '''
        output = run_test([3, 5, 8], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)


# user and dealer have hand_value less than or equal to 21. 
# user hand_value is 17, dealer hand_value is 19. DEALER WILL WIN.
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_output_possibility_1(self, input_mock, randint_mock):
        output_possible_1 = run_test([3, 10, 4], ['y', 'n'], [1, 5, 3], randint_mock, input_mock)
        expected_output_1 = "-----------\n" \
                            "YOUR TURN\n" \
                            "-----------\n" \
                            "Drew a 3\n" \
                            "Drew a 10\n" \
                            "You have 13. Hit (y/n)? y\n" \
                            "Drew a 4\n" \
                            "You have 17. Hit (y/n)? n\n" \
                            "Final hand: 17.\n" \
                            "-----------\n" \
                            "DEALER TURN\n" \
                            "-----------\n" \
                            "Drew an Ace\n" \
                            "Drew a 5\n" \
                            "Dealer has 16.\n" \
                            "Drew a 3\n" \
                            "Final hand: 19.\n" \
                            "-----------\n" \
                            "GAME RESULT\n" \
                            "-----------\n" \
                            "Dealer wins!\n"
        self.assertEqual(output_possible_1, expected_output_1)


# user and dealer have hand_value less than or equal to 21. 
# user hand_value is 19, dealer has Blackjack. DEALER WILL WIN. 
    @patch('blackjack_helper.randint')
    @patch('builtins.input')                        
    def test_output_possibility_2(self, input_mock, randint_mock):
        output_possible_2 = run_test([1, 8], ['x', 'n'], [5, 8, 8], randint_mock, input_mock) 
        expected_output_2 = "-----------\n" \
                            "YOUR TURN\n" \
                            "-----------\n" \
                            "Drew an Ace\n" \
                            "Drew an 8\n" \
                            "You have 19. Hit (y/n)? x\n" \
                            "Sorry I didn't get that.\n" \
                            "You have 19. Hit (y/n)? n\n" \
                            "Final hand: 19.\n" \
                            "-----------\n" \
                            "DEALER TURN\n" \
                            "-----------\n" \
                            "Drew a 5\n" \
                            "Drew an 8\n" \
                            "Dealer has 13.\n" \
                            "Drew an 8\n" \
                            "Final hand: 21.\n" \
                            "BLACKJACK!\n" \
                            "-----------\n" \
                            "GAME RESULT\n" \
                            "-----------\n" \
                            "Dealer wins!\n"
        self.assertEqual(output_possible_2, expected_output_2)  


# user and dealer have hand_value less than or equal to 21. 
# user hand_value is 20, dealer hand_value is 18. USER WILL WIN.
    @patch('blackjack_helper.randint')
    @patch('builtins.input')                       
    def test_output_possibility_3(self, input_mock, randint_mock):
        output_possible_3 = run_test([11, 6, 4], ['y', 'n'], [3, 5, 10], randint_mock, input_mock) 
        expected_output_3 = "-----------\n" \
                            "YOUR TURN\n" \
                            "-----------\n" \
                            "Drew a Jack\n" \
                            "Drew a 6\n" \
                            "You have 16. Hit (y/n)? y\n" \
                            "Drew a 4\n" \
                            "You have 20. Hit (y/n)? n\n" \
                            "Final hand: 20.\n" \
                            "-----------\n" \
                            "DEALER TURN\n" \
                            "-----------\n" \
                            "Drew a 3\n" \
                            "Drew a 5\n" \
                            "Dealer has 8.\n" \
                            "Drew a 10\n" \
                            "Final hand: 18.\n" \
                            "-----------\n" \
                            "GAME RESULT\n" \
                            "-----------\n" \
                            "You win!\n"
        self.assertEqual(output_possible_3, expected_output_3)

        
# user and dealer have hand_value less than or equal to 21. 
# user has Blackjack, dealer hand_value is  19. USER WILL WIN.
    @patch('blackjack_helper.randint')
    @patch('builtins.input')                        
    def test_output_possibility_4(self, input_mock, randint_mock):
        output_possible_4 = run_test([7, 2, 12, 2 ], ['y', 'y'], [10, 7], randint_mock, input_mock)
        expected_output_4 = "-----------\n" \
                            "YOUR TURN\n" \
                            "-----------\n" \
                            "Drew a 7\n" \
                            "Drew a 2\n" \
                            "You have 9. Hit (y/n)? y\n" \
                            "Drew a Queen\n" \
                            "You have 19. Hit (y/n)? y\n" \
                            "Drew a 2\n" \
                            "Final hand: 21.\n" \
                            "BLACKJACK!\n" \
                            "-----------\n" \
                            "DEALER TURN\n" \
                            "-----------\n" \
                            "Drew a 10\n" \
                            "Drew a 7\n" \
                            "Final hand: 17.\n" \
                            "-----------\n" \
                            "GAME RESULT\n" \
                            "-----------\n" \
                            "You win!\n"
        self.assertEqual(output_possible_4, expected_output_4)

        
# user and dealer have hand_value less than or equal to 21. 
# user hand_value is 19, dealer hand_value is 19. NOBOBY WINS, IT'S A PUSH.
    @patch('blackjack_helper.randint')
    @patch('builtins.input')                        
    def test_output_possibility_5(self, input_mock, randint_mock):
        output_possible_5 = run_test([11, 2, 7], ['y', 'n'], [7, 7, 5], randint_mock, input_mock) 
        expected_output_5 = "-----------\n" \
                            "YOUR TURN\n" \
                            "-----------\n" \
                            "Drew a Jack\n" \
                            "Drew a 2\n" \
                            "You have 12. Hit (y/n)? y\n" \
                            "Drew a 7\n" \
                            "You have 19. Hit (y/n)? n\n" \
                            "Final hand: 19.\n" \
                            "-----------\n" \
                            "DEALER TURN\n" \
                            "-----------\n" \
                            "Drew a 7\n" \
                            "Drew a 7\n" \
                            "Dealer has 14.\n" \
                            "Drew a 5\n" \
                            "Final hand: 19.\n" \
                            "-----------\n" \
                            "GAME RESULT\n" \
                            "-----------\n" \
                            "Push.\n"
        self.assertEqual(output_possible_5, expected_output_5)
        

# user and dealer have hand_value less than or equal to 21. 
# user has Blackjack, dealer has Blackjack. NOBODY WINS, IT'S A PUSH.
    @patch('blackjack_helper.randint')
    @patch('builtins.input')                       
    def test_output_possibility_6(self, input_mock, randint_mock):
        output_possible_6 = run_test([11, 1], ['n'], [4, 7, 13], randint_mock, input_mock)  
        expected_output_6 = "-----------\n" \
                            "YOUR TURN\n" \
                            "-----------\n" \
                            "Drew a Jack\n" \
                            "Drew an Ace\n" \
                            "Final hand: 21.\n" \
                            "BLACKJACK!\n" \
                            "-----------\n" \
                            "DEALER TURN\n" \
                            "-----------\n" \
                            "Drew a 4\n" \
                            "Drew a 7\n" \
                            "Dealer has 11.\n" \
                            "Drew a King\n" \
                            "Final hand: 21.\n" \
                            "BLACKJACK!\n" \
                            "-----------\n" \
                            "GAME RESULT\n" \
                            "-----------\n" \
                            "Push.\n"
        self.assertEqual(output_possible_6, expected_output_6)


# user hand_value is greater than 22 or dealer hand_value is greater than 21 or user hand_value and dealer hand_value is greater than 21. 
# user hand_value is 22 (a Bust), dealer hand_value is 19. DEALER WILL WIN.
    @patch('blackjack_helper.randint')
    @patch('builtins.input')                        
    def test_output_possibility_7(self, input_mock, randint_mock):
        output_possible_7 = run_test([13, 2, 10], ['y', 'n'], [8, 1], randint_mock, input_mock) 
        expected_output_7 = "-----------\n" \
                            "YOUR TURN\n" \
                            "-----------\n" \
                            "Drew a King\n" \
                            "Drew a 2\n" \
                            "You have 12. Hit (y/n)? y\n" \
                            "Drew a 10\n" \
                            "Final hand: 22.\n" \
                            "BUST.\n" \
                            "-----------\n" \
                            "DEALER TURN\n" \
                            "-----------\n" \
                            "Drew an 8\n" \
                            "Drew an Ace\n" \
                            "Final hand: 19.\n" \
                            "-----------\n" \
                            "GAME RESULT\n" \
                            "-----------\n" \
                            "Dealer wins!\n"
        self.assertEqual(output_possible_7, expected_output_7)

        
# user hand_value is greater than 22 or dealer hand_value is greater than 21 or user hand_value and dealer hand_value is greater than 21. 
# user hand_value is 27 (a bust), dealer has Blackjack. DEALER WILL WIN.
    @patch('blackjack_helper.randint')
    @patch('builtins.input')                        
    def test_output_possibility_8(self, input_mock, randint_mock):
        output_possible_8 = run_test([5, 1, 1], ['y', 'n'], [7, 4, 10], randint_mock, input_mock)
        expected_output_8 = "-----------\n" \
                            "YOUR TURN\n" \
                            "-----------\n" \
                            "Drew a 5\n" \
                            "Drew an Ace\n" \
                            "You have 16. Hit (y/n)? y\n" \
                            "Drew an Ace\n" \
                            "Final hand: 27.\n" \
                            "BUST.\n" \
                            "-----------\n" \
                            "DEALER TURN\n" \
                            "-----------\n" \
                            "Drew a 7\n" \
                            "Drew a 4\n" \
                            "Dealer has 11.\n" \
                            "Drew a 10\n" \
                            "Final hand: 21.\n" \
                            "BLACKJACK!\n" \
                            "-----------\n" \
                            "GAME RESULT\n" \
                            "-----------\n" \
                            "Dealer wins!\n"
        self.assertEqual(output_possible_8, expected_output_8)

        
# user hand_value is greater than 22 or dealer hand_value is greater than 21 or user hand_value and dealer hand_value is greater than 21. 
# user hand_value is 26 (a Bust), dealer hand_value is 24 (a Bust). DEALER WILL WIN.
    @patch('blackjack_helper.randint')
    @patch('builtins.input')                        
    def test_output_possibility_9(self, input_mock, randint_mock):
        output_possible_9 = run_test([7, 8, 1], ['y', 'n'], [8, 5, 1], randint_mock, input_mock)
        expected_output_9 = "-----------\n" \
                            "YOUR TURN\n" \
                            "-----------\n" \
                            "Drew a 7\n" \
                            "Drew an 8\n" \
                            "You have 15. Hit (y/n)? y\n" \
                            "Drew an Ace\n" \
                            "Final hand: 26.\n" \
                            "BUST.\n" \
                            "-----------\n" \
                            "DEALER TURN\n" \
                            "-----------\n" \
                            "Drew an 8\n" \
                            "Drew a 5\n" \
                            "Dealer has 13.\n" \
                            "Drew an Ace\n" \
                            "Final hand: 24.\n" \
                            "BUST.\n" \
                            "-----------\n" \
                            "GAME RESULT\n" \
                            "-----------\n" \
                            "Dealer wins!\n"
        self.assertEqual(output_possible_9, expected_output_9)
        

# user hand_value is greater than 22 or dealer hand_value is greater than 21 or user hand_value and dealer hand_value is greater than 21. 
# user hand_value is 26 (A Bust) and dealer hand_value is 26(A Bust). They are equal. DEALER WILL STILL WIN.
    @patch('blackjack_helper.randint')
    @patch('builtins.input')                        
    def test_output_possibility_10(self, input_mock, randint_mock):
        output_possible_10 = run_test([1, 5, 10], ['y'], [8, 8, 13], randint_mock, input_mock) 
        expected_output_10 = "-----------\n" \
                             "YOUR TURN\n" \
                             "-----------\n" \
                             "Drew an Ace\n" \
                             "Drew a 5\n" \
                             "You have 16. Hit (y/n)? y\n" \
                             "Drew a 10\n" \
                             "Final hand: 26.\n" \
                             "BUST.\n" \
                             "-----------\n" \
                             "DEALER TURN\n" \
                             "-----------\n" \
                             "Drew an 8\n" \
                             "Drew an 8\n" \
                             "Dealer has 16.\n" \
                             "Drew a King\n" \
                             "Final hand: 26.\n" \
                             "BUST.\n" \
                             "-----------\n" \
                             "GAME RESULT\n" \
                             "-----------\n" \
                             "Dealer wins!\n"
        self.assertEqual(output_possible_10, expected_output_10)


# user hand_value is greater than 22 or dealer hand_value is greater than 21 or user hand_value and dealer hand_value is greater than 21. 
# user hand_value is 18, dealer hand_value is 26 (A Bust). USER WILL WIN.
    @patch('blackjack_helper.randint')
    @patch('builtins.input')                        
    def test_output_possibility_11(self, input_mock, randint_mock):
        output_possible_11 = run_test([1, 7], ['n'], [8, 8, 13], randint_mock, input_mock)
        expected_output_11 = "-----------\n" \
                             "YOUR TURN\n" \
                             "-----------\n" \
                             "Drew an Ace\n" \
                             "Drew a 7\n" \
                             "You have 18. Hit (y/n)? n\n" \
                             "Final hand: 18.\n" \
                             "-----------\n" \
                             "DEALER TURN\n" \
                             "-----------\n" \
                             "Drew an 8\n" \
                             "Drew an 8\n" \
                             "Dealer has 16.\n" \
                             "Drew a King\n" \
                             "Final hand: 26.\n" \
                             "BUST.\n" \
                             "-----------\n" \
                             "GAME RESULT\n" \
                             "-----------\n" \
                             "You win!\n"
        self.assertEqual(output_possible_11, expected_output_11)   


# user hand_value is greater than 22 or dealer hand_value is greater than 21 or user hand_value and dealer hand_value is greater than 21. 
# user has Blackjack, dealer hand_value is 22 (A Bust). USER WILL WIN.
    @patch('blackjack_helper.randint')
    @patch('builtins.input')                        
    def test_output_possibility_12(self, input_mock, randint_mock):
        output_possible_12 = run_test([9, 2, 2, 3, 5], ['y', 'y', 'y'], [2, 2, 7, 4, 7], randint_mock, input_mock) 
        expected_output_12 = "-----------\n" \
                             "YOUR TURN\n" \
                             "-----------\n" \
                             "Drew a 9\n" \
                             "Drew a 2\n" \
                             "You have 11. Hit (y/n)? y\n" \
                             "Drew a 2\n" \
                             "You have 13. Hit (y/n)? y\n" \
                             "Drew a 3\n" \
                             "You have 16. Hit (y/n)? y\n" \
                             "Drew a 5\n" \
                             "Final hand: 21.\n" \
                             "BLACKJACK!\n" \
                             "-----------\n" \
                             "DEALER TURN\n" \
                             "-----------\n" \
                             "Drew a 2\n" \
                             "Drew a 2\n" \
                             "Dealer has 4.\n" \
                             "Drew a 7\n" \
                             "Dealer has 11.\n" \
                             "Drew a 4\n" \
                             "Dealer has 15.\n" \
                             "Drew a 7\n" \
                             "Final hand: 22.\n" \
                             "BUST.\n" \
                             "-----------\n" \
                             "GAME RESULT\n" \
                             "-----------\n" \
                             "You win!\n"
        self.assertEqual(output_possible_12, expected_output_12)
   


if __name__ == '__main__':
    main()