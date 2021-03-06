# phil welsby - 11 jan 2021
# function to ask a question


# NOTE to edit this file you need to fill in the following things:
# 1) The question string
# 2) The correct_answer string
# 3) The wrong_answer string
# 4) The not_valid_answers list
# 5)The line that starts if ans = ''         put the letter for the correct answer between the quotes
#                                            MUST BE LOWER CASE ie a b c or d
#                                            this line is marked with a NOTE below

from time import sleep
import sys

# function which asks a question
def question_1():

# question string
    question = '''
The song Thriller by Micheal Jackson released on
January 23, 1984 as the seventh and final single
from Jackson's sixth studio album was written by
Rodney Lynn Temperton.

But where did  Rodney live?

A) London                       B) Cleethorpes


C) Manchester                   D) Los Angeles
'''
# correct answer string
    correct_answer = '''
Correct Rodney Lynn Temperton (9 October 1949 – 25 September 2016)
commonly and professionally known as Rod Temperton, and informally
known within music circles as 'The Invisible Man', was an English
songwriter, musician, vocalist, and record producer born in 
Cleethorpes Lincolnshire England.
'''
# wrong answer string
    wrong_answer = '''
Wrong  Rodney Lynn Temperton (9 October 1949 – 25 September 2016)
commonly and professionally known as Rod Temperton, and informally
known within music circles as 'The Invisible Man', was an English
songwriter, musician, vocalist, and record producer born in
Cleethorpes Lincolnshire England.
'''

# for loop prints question on the screen
    not_valid_answers = ['a', 'b', 'd']        # list that contains the answers that are not valid
    for i in question:
        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(0.03)

    ans = input('\n\nEnter your answer here :') # get answer from contestant
    ans = ans.lower()
    if ans == 'b':                              # NOTE this line matches the correct answer in the question
        for i in correct_answer:
            sys.stdout.write(i)
            sys.stdout.flush()
            sleep(0.03)
    elif ans in not_valid_answers:    # check to see if answer is not_valid_answers list  ie is it A B C or D
        for i in wrong_answer:        # run if answer is wrong
            sys.stdout.write(i)
            sys.stdout.flush()
            sleep(0.03)
    else:
        print('Your answer must be A B C or D')     # advise player they have entered an invalid answer ie A B C or D
        sleep(2)
        question_1()

# call function
question_1()
