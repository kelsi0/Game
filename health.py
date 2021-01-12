# phil welsby - 12 jan 2021
# function to monitor players health and deduct points
# uses a global variable called health and interacts
# with the question generator

import webbrowser

health = 1

from time import sleep # NOTE this is in the questions.py file so can be deleted from hare
import sys             # NOTE this is in the questions.py file so can be deleted from hare

def health_monitor(x):
    global health
    #health global variable that starts at 3
    for i in'''
So you got that one wrong did you, need to brush
up on your knowledge pal or you ain't gonna make
it to the end are you buddy? Look at your health
''':

        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(0.03)

    sleep(2)

    for i in'''
Your Health is going down way down. Ooh there's nude
vollyball on the TV. Sorry distracted there
better up your game pal or it'll all gonna be over soon
''':
        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(0.05)
    health -=1
    print('\n\nHealth is now',health)

health_monitor(health)

if health == 0:
    webbrowser.open('https://www.youtube.com/watch?v=Fe93CLbHjxQ')


