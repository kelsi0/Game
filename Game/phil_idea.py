# phil welsby - 9 jan 2021
# scrolling opening credits
# sources for sys (https://docs.python.org/3/library/sys.html)
# import modules
# use of [from time import sleep] imports just the sleep bit from time
# hence the use of sleep(0.03) and not time.sleep(0.03)
# also notice that the value of sleep is a float.
from time import sleep
import sys
# this is a for loop
# the use of triple quotes allows you to print on multiple lines
for each_letter in '''
These are the opening credits-
Welcome NOT GOT A NAME FOR THE GAME YET
BUT TEAM  4 RULE!!!!\n
Be Afraid
Be Very Afraid\n
''':
    # this is the bit that does the scrolling of text on the screen
    sys.stdout.write(each_letter)
#    sys.stdout.flush()
    sleep(0.03)
for a in '''
George`
Mika
Kelsey-Team Leader
Phil
Fahad\n''':
    sys.stdout.write(a)
    sys.stdout.flush()
    sleep(0.03)
sleep(3)
for a in '''
Oh! and Jay.... But he may be late haha
[soz dude couldn\'t resist.]\n''':
    sys.stdout.write(a)
    sys.stdout.flush()
    sleep(0.03)
### first attempt a t writing a text based game
### phi welsby - 9 jan 2021
##
import sys
from time import sleep
# plan of house
plan = '''
  ---------------------------------------------------------------------------------
  |                                        |                                      |
  |                                        |                                      |
  |                                        |                                      |
  |                                        |                                      |
  |                                        |                                      |
  |             Kitchen                    |           Living Room
  |                                        |
  |
  |                                                                               |
  |                                                                               |
  |                                        |                                      |
  |----------------------------------------|------------------------------        |
  |                                        |                                      |
  |                                                                               |
  |                                                                               |
  |                    Study               |            Library                   |
  |                                        |                                      |
  |                                        |                                      |
  |                                        |                                      |
  ---------------------------------------------------------------------------------
'''
# opening credits
for a in '''
You are outside the old haunted house of the Scroggins family
All are now dead but legend has it that their spirits remain
and anyone who enters will be cursed for all eternity.
The door is open and is to your left, Do you dare to enter?
\n
Be Afraid
Be Very Afraid\n
''':
   sys.stdout.write(a)
   sys.stdout.flush()
   sleep(0.03)
def start_game():
    try:
        enter = input('Do you dare enter? ')
        enter = enter.lower()
        if enter == 'y' or enter == 'yes':
            enter_house()
        elif enter == 'n' or enter == 'no':
            for a in '''If you don't want to enter why did you say you wanted to play the game...Goodbye\n''':
                   sys.stdout.write(a)
                   sys.stdout.flush()
                   sleep(0.03)
        else:
            print('You need to answer yes or no')
            start_game()
    except ValueError:
            print('Game has Crashed')
def enter_house():
   print(plan)
   for a in '''
You are in the living room, the Library is South the Kitchen is West which way do you wish to go?
Your choices are S W and E. Which way would you like to go? ''':
        sys.stdout.write(a)
        sys.stdout.flush()
        sleep(0.03)
start_game()
input()
print('That\s all folks!!')