from time import sleep
import sys

# function which asks a question
def question(question, correct_answer, wrong_answer, expected_answer):

    for i in question:

        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(0.03)

    ans = input('\n\nEnter your answer here : ') # get answer from contestant
    ans = ans.lower()
    if ans == expected_answer:          # NOTE this line matches the correct answer in the question
        for i in correct_answer: # NOTE: Run if answer is correct
            sys.stdout.write(i)
            sys.stdout.flush()
            sleep(0.03)
    else:
        for i in wrong_answer:  # NOTE: Run if answer is wrong
            sys.stdout.write(i)
            sys.stdout.flush()
            sleep(0.03)

question('''
Who is England's all time top goal scorer?

A)  Bobby CHarlton      B)  Gary Lineker

C)  Wayne Rooney        D)  Alan Shearer

''','''
Correct! Wayne Rooney overtook Bobby Charlton's recored of 49 international goals on Tuesday 8th September 2015.
''','''
Wrong! Wayne Rooney overtook Bobby Charlton's recored of 49 international goals on Tuesday 8th September 2015.
''',
'c')

question('''
Who holds the record for most appearances in the Premier League?

A)  Ryan Giggs          B)  Gareth Barry

C)  James Milner        D)  David James

''','''
Correct! Gareth Barry holds the record after 653 career Premier League appearances for Aston Villa, Manchester City, Everton & West Brom.
''','''
Wrong! Gareth Barry holds the record after 653 career Premier League appearances for Aston Villa, Manchester City, Everton & West Brom.
''',
'b')

question('''
Who was the first person in space?

A)  Yuri gagarin        B) Buzz Aldrin

C)  Neil Armstrong      D) Alan Shepherd

''','''
Correct! Although Neil Armstrong was the first man on the moon and Alan Shepherd was the first American in space, Yuri Gagarin was the first person to go into space.
''','''
Wrong! Although Neil Armstrong was the first man on the moon and Alan Shepherd was the first American in space, Yuri Gagarin was the first person to go into space.
''',
'a')

question('''
Which nation has won the most World Cups?

A)  Italy               B) France

C)  Germany             D) Brazil

''','''
Correct! Brazil have won the most World Cups with 5, despite not winning any of the last 4 tournaments.
''','''
Wrong! Brazil have won the most World Cups with 5, despite not winning any of the last 4 tournaments.
''',
'd')

question('''
Which of these is not a metal?

A)  Magnesium           B) Lithium

C)  Uranium             D) Nitrogen

''','''
Correct! Nitrogen is the only element that is not a metal.
''','''
Wrong! Nitrogen is the only element that is not a metal.
''',
'd')

