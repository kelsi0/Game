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