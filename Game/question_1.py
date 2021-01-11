# phil welsby - 11 jan 2021
# function to ask a question

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

# # function which asks a question
# def question_2():

# # question
    # question = '''
# What colour is the solid form of oxygen?
# A)Red                          B)Green

# C)Yellow                       D)Blue
# '''
# # correct answer
#     correct_answer = '''
# Correct! The solid colour for of oxygen is infact blue.
# '''
# # wrong answer
#     wrong_answer = '''
# Wrong! The solid colour for of oxygen is infact blue
# '''

# # for loop prints question on the screen
#     for i in question:

#         sys.stdout.write(i)
#         sys.stdout.flush()
#         sleep(0.03)

#     ans = input('\n\nEnter your answer here :') # get answer from contestant
#     ans = ans.lower()
#     if ans == 'd':          # NOTE this line matches the correct answer in the question
#         for i in correct_answer: # run if answer is correct
#             sys.stdout.write(i)
#             sys.stdout.flush()
#             sleep(0.03)
#     else:
#         for i in wrong_answer:  # run if answer is wrong
#             sys.stdout.write(i)
#             sys.stdout.flush()
#             sleep(0.03)



# # function which asks a question
# def question_3():

# # question
#     question = '''
# What colour is the sunset on Mars?
# A)Red                          B)Green

# C)Blue                         D)Orange
# '''
# # correct answer
#     correct_answer = '''
# Correct! The sunset on mars is blue (And really cool!).
# '''
# # wrong answer
#     wrong_answer = '''
# Wrong! The sunset on mars is blue (And really cool!).
# '''

# # for loop prints question on the screen
#     for i in question:

#         sys.stdout.write(i)
#         sys.stdout.flush()
#         sleep(0.03)

#     ans = input('\n\nEnter your answer here :') # get answer from contestant
#     ans = ans.lower()
#     if ans == 'c':          # NOTE this line matches the correct answer in the question
#         for i in correct_answer: # run if answer is correct
#             sys.stdout.write(i)
#             sys.stdout.flush()
#             sleep(0.03)
#     else:
#         for i in wrong_answer:  # run if answer is wrong
#             sys.stdout.write(i)
#             sys.stdout.flush()
#             sleep(0.03)

# # function which asks a question
# def question_4():

# question
#     question = '''
# Which part of the human body does not have a blood supply?
# A) Kneecap                    B)Earlobe

# C)Fingernails                 D)Cornea
# '''
# # correct answer
#     correct_answer = '''
# Correct! The cornea have no blood supply!.
# '''
# # wrong answer
#     wrong_answer = '''
# Wrong! The cornea have no blood supply!.
# '''

# # for loop prints question on the screen
#     for i in question:

#         sys.stdout.write(i)
#         sys.stdout.flush()
#         sleep(0.03)

#     ans = input('\n\nEnter your answer here :') # get answer from contestant
#     ans = ans.lower()
#     if ans == 'd':          # NOTE this line matches the correct answer in the question
#         for i in correct_answer: # run if answer is correct
#             sys.stdout.write(i)
#             sys.stdout.flush()
#             sleep(0.03)
#     else:
#         for i in wrong_answer:  # run if answer is wrong
#             sys.stdout.write(i)
#             sys.stdout.flush()
#             sleep(0.03)

# # function which asks a question
# def question_5():

# # question
#     question = '''
# In 2015, Merlin the rescue cat set a new world record for what?
# A)Longest Fur                 B)Loudest Purr

# C)Best Mouser                 D)Heaviest Cat
# '''
# # correct answer
#     correct_answer = '''
# Correct! The most adorable world record ever for the loudest purr.
# '''
# # wrong answer
#     wrong_answer = '''
# Wrong! The most adorable world record ever for the loudest purr.
# '''

# # for loop prints question on the screen
#     for i in question:

#         sys.stdout.write(i)
#         sys.stdout.flush()
#         sleep(0.03)

#     ans = input('\n\nEnter your answer here :') # get answer from contestant
#     ans = ans.lower()
#     if ans == 'b':          # NOTE this line matches the correct answer in the question
#         for i in correct_answer: # run if answer is correct
#             sys.stdout.write(i)
#             sys.stdout.flush()
#             sleep(0.03)
#     else:
#         for i in wrong_answer:  # run if answer is wrong
#             sys.stdout.write(i)
#             sys.stdout.flush()
#             sleep(0.03)




# # call function
# question_1()
# question_2()
# question_3()
# question_4()
# question_5()
