#
#
#
#
#
#
#
from time import sleep
import sys
import os
os.system('clear')
sleep(1)

for i in '''
                      .-.            .-.             .-.            .-.             .-.            .-.       
                    _/@@ \          /aa \_         _/xx \          /aa \_         _/oo \          /^^ \_     
                   ( \o  /__      __\-  / )       ( \¬  /__      __\-  / )       ( \o  /__      __\-  / )    
         /          \/   ___)    (__/    /         \/   ___)    (__/    /         \/   ___)    (__/    /     
         \o_        /     \        /     \         /     \        /     \         /     \        /     \     
           \|      / george\_     / fahad \__     / phil  \_     / mika  \__     / kelsey\_     /  jay  \__  
           /\/     \_.-.__   )    \_.-._._   )    \_.-.__   )    \_.-._._   )    \_.-.__   )    \_.-._._ )   
          \              '-'             `-`            '-'             `-`            '-'             `-`   
''':
    sys.stdout.write(i)
    sys.stdout.flush()
    sleep(0.0045)

sleep(2)
print('\n\n\n')


#print("\n               .-.            .-.             .-.            .-.             .-.            .-.       ")
#print("             _/@@ \          /aa \_         _/xx \          /aa \_         _/oo \          /^^ \_     ")
#print("            ( \o  /__      __\-  / )       ( \¬  /__      __\-  / )       ( \o  /__      __\-  / )    ")
#print("  /          \/   ___)    (__/    /         \/   ___)    (__/    /         \/   ___)    (__/    /     ")
#print("  \o_        /     \        /     \         /     \        /     \         /     \        /     \     ")
#print("    \|      / george\_     / fahad \__     / phil  \_     / mika  \__     / kelsey\_     /  jay  \__  ")
#print("    /\/     \_.-.__   )    \_.-._._   )    \_.-.__   )    \_.-._._   )    \_.-.__   )    \_.-._._   ) ")
#print("    \              '-'             `-`            '-'             `-`            '-'             `-`  ")





# phil welsby - 12 jan 2021
# Mika Shyu


# import
import sys
from time import sleep




# for loop to scroll credits onto the screen
# using tripple quotes allows you to print over multiple lines
for i in '''
Opening Credits By Mika Shyu


	Welcome to the Haunted Mansion.
	Are you brave enough to enter the Haunted Mansion?
	Once you go in there is no turning back.
	Let's get started.\n\n
''':

    sys.stdout.write(i)
    sys.stdout.flush()
    sleep(0.03)

# NOTE -  need to develop and input to accept the player name here


# # NOTE - code required to ask player if they want to play y/n


# pause
input('\nPress Enter  Continue >>> ')  #NOTE - used used to pause game whilst developing
print('\n\n')





for i in ''' You awake in a dimly lit room, vaguely aware of a throbbing coming from somewhere deep in your head, or is it below you in the house?''':
    sys.stdout.write(i)
    sys.stdout.flush()
    sleep(0.03)


# used just sleep here because at top we used   from time impor sleep
sleep(2)

for i in '''
You push yourself up off the filthy rotting floorboards and hear the scuttle of what you hope is a rat. There is enough moonlight filtering
in through the thick dusty curtains to make out what appears to be 4 doors. Each scraw''':
    sys.stdout.write(i)
    sys.stdout.flush()
    sleep(0.03)

sleep(2)
for i in '''
The wind howls and rattles the thin window panes but then you realise that the howling is coming from inside the house. The dust picks up 
around you and a show detaches itself from the rest.''':

    sys.stdout.write(i)
    sys.stdout.flush()
    sleep(0.03)
sleep(2)
for i in '''The figure in front of you is that of a tall thin man wearing a beanie and frameless glasses. You are frozen with fright. He bends, until 
     his face is inches from your own and he asks ***** There is another gust of wind and you''':
    sys.stdout.write(i)
    sys.stdout.flush()
    sleep(0.03)
sleep(2)
for i in '''You look at the doors and choose which to go through. A,B,C or D")''':
    sys.stdout.write(i)
    sys.stdout.flush()
    sleep(0.03)








