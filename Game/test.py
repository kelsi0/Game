from time import sleep
import sys

# function which asks a question
def question(question, correct_answer, wrong_answer, expected_ans):

# for loop prints question on the screen
    for i in question:

        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(0.03)

    ans = input('\n\nEnter your answer here :') # get answer from contestant
    ans = ans.lower()
    if ans == expected_ans:          # NOTE this line matches the correct answer in the question
        for i in correct_answer: # run if answer is correct
            sys.stdout.write(i)
            sys.stdout.flush()
            sleep(0.03)
    else:
        for i in wrong_answer:  # run if answer is wrong
            sys.stdout.write(i)
            sys.stdout.flush()
            sleep(0.03)

question('''
What body parts do northern leopard frogs use to help swallow their prey?

A)Feet                         B)Eyes

C)Ears                         D)Nostrils
''','''
Correct! Northern leopard frogs use their ears to help swallow their prey.
''','''
Wrong!  Northern leopard frogs use their ears to help swallow their prey.
''','''b''')

# question('''What colour is the solid form of oxygen?
# A)Red                          B)Green

# C)Yellow                       D)Blue
# ''',''' 
# Correct! The solid colour for of oxygen is infact blue.
#  ''','''
# Wrong! The solid colour for of oxygen is infact blue''','''d''')

# question('''
# What colour is the sunset on Mars?
# A)Red                          B)Green

# C)Blue                         D)Orange
# ''','''
# Correct! The sunset on mars is blue (And really cool!).
# ''','''
# Wrong! The sunset on mars is blue (And really cool!).
# ''','''c''')

# question('''
# Which part of the human body does not have a blood supply?
# A) Kneecap                    B)Earlobe

# C)Fingernails                 D)Cornea
# ''','''
# Correct! The cornea have no blood supply!.
# ''','''
# Wrong! The cornea have no blood supply!.
# ''','''d''')

# question('''
# In 2015, Merlin the rescue cat set a new world record for what?
# A)Longest Fur                 B)Loudest Purr

# C)Best Mouser                 D)Heaviest Cat
# ''','''
# Correct! The most adorable world record ever for the loudest purr.
# ''','''
# Wrong! The most adorable world record ever for the loudest purr.
# ''','''b''')

