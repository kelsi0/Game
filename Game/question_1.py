# phil welsby - 11 jan 2021
# function to ask a question

from time import sleep
import sys

# function which asks a question
def question_1():

# question
    question = '''
The song Thriller by Micheal Jackson released on
January 23, 1984 as the seventh and final single
from Jackson's sixth studio album was written by
Rodney Lynn Temperton.

But where did  Rodney live?

A) London                       B) Cleethorpes


C) Manchester                   D) Los Angeles
'''
# correct answer
    correct_answer = '''
Correct Rodney Lynn Temperton (9 October 1949 – 25 September 2016)
commonly and professionally known as Rod Temperton, and informally
known within music circles as 'The Invisible Man', was an English
songwriter, musician, vocalist, and record producer born in 
Cleethorpes Lincolnshire England.
'''
# wrong answer
    wrong_answer = '''
Wrong  Rodney Lynn Temperton (9 October 1949 – 25 September 2016)
commonly and professionally known as Rod Temperton, and informally
known within music circles as 'The Invisible Man', was an English
songwriter, musician, vocalist, and record producer born in
Cleethorpes Lincolnshire England.
'''

# for loop prints question on the screen
    for i in question:

        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(0.03)

    ans = input('\n\nEnter your answer here :') # get answer from contestant
    ans = ans.lower()
    if ans == 'b':          # NOTE this line matches the correct answer in the question
        for i in correct_answer: # run if answer is correct
            sys.stdout.write(i)
            sys.stdout.flush()
            sleep(0.03)
    else:
        for i in wrong_answer:  # run if answer is wrong
            sys.stdout.write(i)
            sys.stdout.flush()
            sleep(0.03)

# call function
question_1()
