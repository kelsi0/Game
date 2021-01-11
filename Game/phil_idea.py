from time import sleep
import sys

# function which asks a question
def question_16(question, correct_answer, wrong_answer, expected_ans):

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

question_16('''
What was William Shakespeare's last play called?

A)The Tempest                  B)A Midsummer Night's Dream

C)Romeo and Juliet             D)As you like it
''','''
Correct - Legend has it that this is the first of two plays Shakespeare wrote for a mysterious figure that gifted him his powers of writing.
''','''
Wrong!  Perhaps you should reaquaint yourself with the Bard from Stratford upon Avon.
''',
'''a''')
def question_17(question, correct_answer, wrong_answer, expected_ans):
    for i in question:

        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(0.03)

    ans = input('\n\nEnter your answer here :') # get answer from contestant
    ans = ans.lower()
    if ans == expected_ans:        # NOTE this line matches the correct answer in the question
        for i in correct_answer: # run if answer is correct
            sys.stdout.write(i)
            sys.stdout.flush()
            sleep(0.03)
    else:
        for i in wrong_answer:  # run if answer is wrong
            sys.stdout.write(i)
            sys.stdout.flush()
            sleep(0.03)

question_17('''
What is the primary reason Millennials are unable to buy houses?

A)Poor economic management and policy decision making from the previous generation                B)Corporate greed

C)Avocados            D)The free market
''','''
Correct - Poor money management and lack of get up and go is the reason that many in the 'Millennial' generation are unable to afford houses. Other reasons include: cereal cafes, inability to open a can of beans, being a snowflake and not working as hard as the previous generation, apparently.
''','''
Wrong! Back to the Northern Quarter with you. 
'''
,'''c''')

def question_18(question, correct_answer, wrong_answer, expected_ans):
    for i in question:

        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(0.03)

    ans = input('\n\nEnter your answer here :') # get answer from contestant
    ans = ans.lower()
    if ans == expected_ans:         # NOTE this line matches the correct answer in the question
        for i in correct_answer: # run if answer is correct
            sys.stdout.write(i)
            sys.stdout.flush()
            sleep(0.03)
    else:
        for i in wrong_answer:  # run if answer is wrong
            sys.stdout.write(i)
            sys.stdout.flush()
            sleep(0.03)

question_18('''
Which of the following video game franchises is the brain child of the famous director Hideo Kojima?

A)Plastic Wrench Liquid  B)Metal Gear Solid

C)Call of Duty           D)Shout of Obligation
''','''
Correct - Despite it's convoluted story and awkward name. Metal Gear Solid remains the defining franchise of the stealth genre.
''','''
Snake what happened? Snake? SSSSSSNNNNNNNNAAAAAAAAAAAAAAAAAAKKKKKKKKKKKKKKKKKKEEEEEEEEEE!
'''
,'''b''')

def question_19(question, correct_answer, wrong_answer, expected_ans):
    for i in question:

        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(0.03)

    ans = input('\n\nEnter your answer here :') # get answer from contestant
    ans = ans.lower()
    if ans == expected_ans:         # NOTE this line matches the correct answer in the question
        for i in correct_answer: # run if answer is correct
            sys.stdout.write(i)
            sys.stdout.flush()
            sleep(0.03)
    else:
        for i in wrong_answer:  # run if answer is wrong
            sys.stdout.write(i)
            sys.stdout.flush()
            sleep(0.03)

question_19('''
Which of the following US Presidents suffered from extreme stage fright?

A)Alexander Hamilton     B)Abraham Lincoln

C)Thomas Jefferson       D)Ulysses Grant
''','''
Correct - Despite his portrayal in the hit musical 'Hamilton' Thomas Jefferson only gave two speeches in his life and even then audiences had to strain to hear him. This was despite kicking ass as the ambassador to France.
''','''
I afraid you will never be president, or in the room where it happens.
'''
,'''c''')

def question_20(question, correct_answer, wrong_answer, expected_ans):
    for i in question:

        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(0.03)

    ans = input('\n\nEnter your answer here :') # get answer from contestant
    ans = ans.lower()
    if ans == expected_ans:       # NOTE this line matches the correct answer in the question
        for i in correct_answer: # run if answer is correct
            sys.stdout.write(i)
            sys.stdout.flush()
            sleep(0.03)
    else:
        for i in wrong_answer:  # run if answer is wrong
            sys.stdout.write(i)
            sys.stdout.flush()
            sleep(0.03)

question_20('''
Recent research suggests that dinosaurs who once ruled the planet has what kind of skin?


A)Leathery               B)Smooth

C)Furry                  D)Feathery
''','''
Correct - Recent research suggests that dinosaurs, as they were more closely related to birds were feathered. Even the fearsome T-Rex is considered to have had feathers along it's head, neck and tail. The velociraptor was about the size of a chicken and feathered as such. Clever girl...
''','''
You have been eaten by a T-Rex.
'''
,'''d''')
