

import question_function  #This imports the information from question_function so we can use it.
import sys
from time import sleep



#This block is how we will call the questions and the consequences for right or wrong.
random_q = question_function.rand_question()   
if random_q >= 0:
    if question_function.question(random_q):
        #We had a question, they got it right. Put what happens next here!
        print('''Progress to the next room.''')
            
    else:
        #They got the answer wrong, put consequences here!
        print('''You twist the door handle, there is a sharp click and you swing it open. You vaguely hear a rapid clicking like an egg timer before you can locate the source of the sound you hear a loud bang from an explosion above your head. The last thing you hear is the sound of your own skull crumpling.''')
else:
    print("I ran out of questions!")