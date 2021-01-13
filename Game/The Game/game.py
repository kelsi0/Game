#Here is where we will write the main code for our game!
#Starting with Mika's intro and then moving into the different rooms ect.
#Please do no put the full code for questions.py or health.py in here, they will be stored in seperate files
#We can call those functions for now and comment it out e.g
#questions()
import question_function  #This imports the information from question_function so we can use it.
import sys
from time import sleep
print("Welcome to the Haunted Mansion.")
# NOTE: Mansion with ghost in background
print('''\n                                            .-.                           
                                          .'   `.                         
                            _____         :g g   :                        
                            )   (         : o    `.                       
                           / oOo \       :         ``.                    
                          /_______\     :             `.                  
                          |       |    :  :         .   `.                
                          |  .-.  |    :   :          ` . `.              
                          |  |~|  |     `.. :            `. ``;           
  I-I-I-I-I-I-I-I-I-I-I-I-|  |_|  |I-I-I-I-I-I-I-I-I-I-I-I-I:'            
  ).**.(~~~~~~~~~~~~~~~~~~|       |~~~~~~~~~~~~~~~~~~~).**.( `.           
 / |  | \                 |       |                  / |  | \  `.     .   
 ) |__| (                _|_.---._|_                 ) |__| (,___`;.-'    
 |______|_________________|' .-. '|__________________|______|             
 |      |  .-.  .-.       |,-|~|-,|        .-.  .-.  |      |             
 \ .    /  |~|  |~|       || | | ||        |~|  |~|  \    . /             
  )H   (   |_|  |_|       ||_|_|_||        |_|  |_|   )   H(              
  |    |                  |       |                   |    |              
  |    |                  |       |                   |    |              
  \    /   ...  ...       |_.=~=._|        ...  ...   \    /              
   ). (    |~|  |~|       |I|   |I|        |~|  |~|    ) .(               
   |H |    |_|  |_|       |I|  .|I|        |_|  |_|    | H|               
   |  |                   |I|___|I|                    |  |               
   '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'               ''')
name = input("To pass into the building the spirits demand a name. Reveal your identity.\n")
play = input(f"So... {name}... \nAre you brave enough to enter the Haunted mansion? Once you go in there is no turning back.\n")
# NOTE: Do they want to play
if play.lower() in ["yes", "y"]:
# NOTE: Question 1
    for i in '''
        You awake in a dimly lit room, vaguely aware of a throbbing coming from somewhere deep in your head, or is it below you in the house? You push yourself up off the filthy rotting floorboards and hear the scuttle of what you hope is a rat. There is enough moonlight filtering in through the thick dusty curtains to make out what appears to be 4 doors. Each scrawled with a letter in what you hope is not blood.
        The wind howls and rattles the thin window panes but then you realise that the howling is coming from inside the house. The dust picks up around you and a show detaches itself from the rest. 
        The figure in front of you is that of a tall thin man wearing a beanie and frameless glasses. You are frozen with fright. He bends, until his face is inches from your own and he asks ***** There is another gust of wind and you are unsure if the apparition of the man was a bad fever dream.
        You look at the doors and choose which to go through. A,B,C or D
        ''':
        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(.005)
        print()
        
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

    print("\n    Door A         Door B         Door C         Door D")
    print("  __________     __________     __________     __________   ")
    print(" |  __  __  |   |  __  __  |   |  __  __  |   |  __  __  |  ")
    print(" | |  ||  | |   | |  ||  | |   | |  ||  | |   | |  ||  | |  ")
    print(" | |  ||  | |   | |  ||  | |   | |  ||  | |   | |  ||  | |  ")
    print(" | |__||__| |   | |__||__| |   | |__||__| |   | |__||__| |  ")
    print(" |  __  __()|   |  __  __()|   |  __  __()|   |  __  __()|  ")
    print(" | |  ||  | |   | |  ||  | |   | |  ||  | |   | |  ||  | |  ")
    print(" | |  ||  | |   | |  ||  | |   | |  ||  | |   | |  ||  | |  ")
    print(" | |  ||  | |   | |  ||  | |   | |  ||  | |   | |  ||  | |  ")
    print(" | |  ||  | |   | |  ||  | |   | |  ||  | |   | |  ||  | |  ")
    print(" | |__||__| |   | |__||__| |   | |__||__| |   | |__||__| |  ")
    print(" |__________|   |__________|   |__________|   |__________|  ")
# NOTE: Question 2
    for i in '''
        Your hand trembles from the cold and you push the door open, how did it get so cold so quickly? Your breath comes quick and frosts in the air in front of you. As you progress into the next room you recognise that it is empty apart from a few old deflated footballs. Above the fireplace you spot a ragged old shirt. As your eyes adjust to the dark you notice that it has been pulled over a shapeless bulk. You stumble further inside. You hope that the bulk did not twitch as you look around the room and that it is a pentagon with 4 additional doors caked in mud and with grass growing in the letters A,B,C and D. You glance back up at the flickering fireplace and notice that the shirt, and the bulk are no longer there. Cautiously you move closer to the fireplace which is steadily dying. It flickers out just as you reach it and the cold descends again.
        Frozen, fetid breath envelops your neck before you turn around and come face to face with the mottled flesh of a young man long dead, a close cut hairstyle now patchy. As he opens his mouth to speak bile, blood and saliva pours down his ripped football shirt. Beneath the rolling eyes his mouth moves spraying you with the disgusting liquid. ***** You take a step back and trip, falling backwards into the fireplace. The logs are surprisingly cold. As you push yourself up, you realise the man has vanished. Squinting, you choose a door.
        ''':
        print("\n               .-.            .-.             .-.            .-.             .-.            .-.       ")
        print("             _/@@ \          /aa \_         _/xx \          /aa \_         _/oo \          /^^ \_     ")
        print("            ( \o  /__      __\-  / )       ( \¬  /__      __\-  / )       ( \o  /__      __\-  / )    ")
        print("  /          \/   ___)    (__/    /         \/   ___)    (__/    /         \/   ___)    (__/    /     ")
        print("  \o_        /     \        /     \         /     \        /     \         /     \        /     \     ")
        print("    \|      / george\_     / fahad \__     / phil  \_     / mika  \__     / kelsey\_     /  jay  \__  ")
        print("    /\/     \_.-.__   )    \_.-._._   )    \_.-.__   )    \_.-._._   )    \_.-.__   )    \_.-._._   ) ")
        print("    \              '-'             `-`            '-'             `-`            '-'             `-`  ")
        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(.005)
        print()

random_q = question_function.rand_question()
if random_q >= 0:
    if question_function.question(random_q):
        #We had a question, they got it right. Put what happens next here!
        print('''Progress to the next room.''')
            
    else:
        #They got the answer wrong, put consequences here!
        print('''You open the door and step into the darkness, it slams shut behind you. You are kicked roughly from one side and then again from the other. Studs breaking your skin. You try to push back but are forced to the floor. You feel your legs and fingers break and are powerless to stop the end. Slowly the bulk from above the fireplace climbs down and pulls your smashed out from behind the door. It kneels over and starts tearing flesh from bone before dragging your remains into the fireplace.''')
else:
    print("I ran out of questions!")



    
        # question(random_q)
        # # NOTE: IF Question 2 is correct
        # if question(random_q) == True: 
        #     for i in '''
        #         Progress to the next room.
        #         ''':
        #         sys.stdout.write(i)
        #         sys.stdout.flush()
        #         sleep(.005)
        #         print()
        # # NOTE: If Question 2 is incorrect
        # else:
        #     for i in '''
        #         You open the door and step into the darkness, it slams shut behind you. You are kicked roughly from one side and then again from the other. Studs breaking your skin. You try to push back but are forced to the floor. You feel your legs and fingers break and are powerless to stop the end. Slowly the bulk from above the fireplace climbs down and pulls your smashed out from behind the door. It kneels over and starts tearing flesh from bone before dragging your remains into the fireplace.
        #         ''':
        #         sys.stdout.write(i)
        #         sys.stdout.flush()
        #         sleep(.005)
        #         print()
# else:
#     print("Get a grip you scared little biiiitch.")