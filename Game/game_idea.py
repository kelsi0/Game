import time

def wrong_answer_bedroom():
    time.sleep(1)
    response = input("Shall we explore the hallway next? [Y/N] ")
    if response == "Y":
        print("Ok, I'm on my way to the hallway!")
        time.sleep(1)
        #hallway()
    elif response == "N":
        print("I can have another look if you want.")
        time.sleep(1)
        bedroom()
    else:
        print("That wasn't an option, please try again!")
        time.sleep(1)
        wrong_answer_bedroom()

def bedroom():
    time.sleep(1)
    print("I can't see any food in here but I have found something that could be useful!")
    time.sleep(1)
    print("You have found *Dog Toy*")
    time.sleep(1)
    response = input("Shall we explore the hallway next? [Y/N] ")
    if response == "Y":
        print("Ok, I'm on my way to the hallway!")
        time.sleep(1)
        hallway()
    elif response == "N":
        print("I can have another look if you want.")
        time.sleep(1)
        bedroom()
    else:
        print("That wasn't an option, please try again!")
        time.sleep(1)
        wrong_answer_bedroom()

def wrong_answer_first_room():
    time.sleep(1)
    response = input("What shall we do first? [Explore the bedroom/Go into the hallway]")
    if response == "Explore the bedroom":
        print("Ok, let's have a look aorund")
        time.sleep(1)
        bedroom()
    elif response == "Go into the hallway":
        print("Ok, let's go together!")
        #hallway()
    else:
        print("That wasn't an option please try again!")
        time.sleep(1)
        wrong_answer_first_room()    

def first_room():
    time.sleep(1)
    print("We appear to be in the bedroom, I can smell food from the hallway.")
    time.sleep(1)
    print("I can't hear much noise at the moment, the dog must be asleep!")
    time.sleep(1)
    response = input("What shall we do first? [Explore the bedroom/Go into the hallway]")
    if response == "Explore the bedroom":
        print("Ok, let's have a look aorund")
        time.sleep(1)
        bedroom()
    elif response == "Go into the hallway":
        print("Ok, let's go together!")
        #hallway()
    else:
        print("That wasn't an option please try again!")
        time.sleep(1)
        wrong_answer_first_room()


def game_intro_wrong():
    time.sleep(1)
    response = input("Will you help me find some food? [Y/N] ")
    if response == "Y":
        print("Thank you! Let's have a look around!")
        first_room()
    elif response == "N":
        print("You will leave me to starve?")
        time.sleep(1)
        game_intro_wrong()
    else:
        print("That wasn't an option, please try again!")
        time.sleep(1)
        game_intro_wrong()      

def game_intro():
    print("""(=^-ω-^=)""")
    time.sleep(1)
    print("Hello! I am Cat, to start please give me a better name!")
    time.sleep(1)
    global cat
    cat = input("What is my name? ")
    time.sleep(1)
    print(f"Thank you! My name is now {cat}.")
    time.sleep(1)
    print("I have just woken up and am very hungry!!")
    time.sleep(1)
    response = input("Will you help me find some food? [Y/N] ")
    if response == "Y":
        print("Thank you! Let's have a look around!")
        first_room()
    elif response == "N":
        print("You will leave me to starve?")
        time.sleep(1)
        game_intro_wrong()
    else:
        print("That wasn't an option, please try again!")
        time.sleep(1)
        game_intro_wrong()

    

game_intro()
