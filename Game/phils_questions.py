from time import sleep
import sys

# function which asks a question
def question_1(question, correct_answer, wrong_answer):

# # question
#     question = '''
# What body parts do northern leopard frogs use to help swallow their prey?

# A)Feet                         B)Eyes

# C)Ears                         D)Nostrils
# '''
# # correct answer
#     correct_answer = '''
# Correct! Northern leopard frogs use their ears to help swallow their prey.
# '''
# # wrong answer
#     wrong_answer = '''
# Wrong!  Northern leopard frogs use their ears to help swallow their prey.
# '''

# for loop prints question on the screen
    for i in question:

        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(0.03)

    ans = input('\n\nEnter your answer here :') # get answer from contestant
    ans = ans.lower()
    if ans == 'c':          # NOTE this line matches the correct answer in the question
        for i in correct_answer: # run if answer is correct
            sys.stdout.write(i)
            sys.stdout.flush()
            sleep(0.03)
    else:
        for i in wrong_answer:  # run if answer is wrong
            sys.stdout.write(i)
            sys.stdout.flush()
            sleep(0.03)

question_1('''
What body parts do northern leopard frogs use to help swallow their prey?
A)Feet                         B)Eyes
C)Ears                         D)Nostrils
''','''
Correct! Northern leopard frogs use their ears to help swallow their prey.
''','''
Wrong!  Northern leopard frogs use their ears to help swallow their prey.
''')



['''
Who is often called the father of the computer?
A) Eben Upton                  B)David Montgomery
C) Charles Babbage             D) William Shockley
''','''
Correct! 
''','''
Wrong! 
''','''c''')] 


['''
Which of these is not a seconday primary colour
A)RED                         B)YELLOW
C)CYAN                        D)MAGENTA
''','''
Correct! The primary colours are RED GREEN and BLUE
and the secondary primaries are MAGENTA CYAN and YELLOW
''','''
Wrong! The primary colours are RED GREEN and BLUE
and the secondary primaries are MAGENTA CYAN and YELLOW
''','''a''')] 


['''
What is the answer to this maths question 2**8
A)256                         B)64
C)1024                        D)512
''','''
Correct! 2 x 2 x 2 x 2 x 2 x 2 x 2 x2  =  256
Two to the power of 8
''','''
Wrong! 2 x 2 x 2 x 2 x 2 x 2 x 2 x2  =  256
Two to the power of 8
''','''a''')] 


['''
What is Morrissey the singer with the Smiths middle name
A)Patrick                     B)Robert
C)Albert                      D)Marvin
''','''
Correct! Morrisseys middle name is Patrick
''','''
Wrong! The most adorable world record ever for the loudest purr.
''','''a''')] 


['''
Who is credited with creating the first compiler for a computer programming language
A)Grace Hopper                 B)Ada Lovelace
C)Dennis Hopper                D)Sophie Wilson
''','''
Correct! Grace Brewster Murray Hopper (née Murray December 9, 1906 – January 1, 1992) 
was an American computer scientist and United States Navy rear admiral.[1] One of the 
first programmers of the Harvard Mark I computer,
''','''
Wrong! Grace Brewster Murray Hopper (née Murray December 9, 1906 – January 1, 1992) 
was an American computer scientist and United States Navy rear admiral.[1] One of the 
first programmers of the Harvard Mark I computer,
''','''a''')] 

