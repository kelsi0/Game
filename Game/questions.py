from random import randint
import random

from time import sleep
import sys

 

list_of_questions = [
    ['''
    What body parts do northern leopard frogs use to help swallow their prey?

    A)Feet                              B)Eyes

    C)Ears                              D)Nostrils
    ''','''
    Correct! Northern leopard frogs use their eyes to help swallow their prey.
    ''','''
    Wrong!  Northern leopard frogs use their eyes to help swallow their prey.
    ''','''b''', False],

    ['''What colour is the solid form of oxygen?

     A)Red                               B)Green

     C)Yellow                            D)Blue
     ''',''' 
     Correct! The solid colour for of oxygen is infact blue.
     ''','''
     Wrong! The solid colour for of oxygen is infact blue''','''d''', False],

     ['''
    What colour is the sunset on Mars?

    A)Red                                B)Green

    C)Blue                               D)Orange
    ''','''
    Correct! The sunset on mars is blue (And really cool!).
    ''','''
    Wrong! The sunset on mars is blue (And really cool!).
    ''','''c''', False],

    ['''
    Which part of the human body does not have a blood supply?

     A) Kneecap                          B)Earlobe

     C)Fingernails                       D)Cornea
    ''','''
     Correct! The cornea have no blood supply!.
    ''','''
    Wrong! The cornea have no blood supply!.
    ''','''d''', False],

    ['''
    In 2015, Merlin the rescue cat set a new world record for what?

    A)Longest Fur                        B)Loudest Purr

    C)Best Mouser                        D)Heaviest Cat
    ''','''
    Correct! The most adorable world record ever for the loudest purr.
    ''','''
    Wrong! The most adorable world record ever for the loudest purr.
    ''','''b''', False],

    ['''
    What was William Shakespeare's last play called?

    A)The Tempest                        B)A Midsummer Night's Dream

    C)Romeo and Juliet                   D)As you like it
    ''','''
    Correct - Legend has it that this is the first of two plays Shakespeare wrote for a mysterious figure that gifted him his powers of writing.
    ''','''
    Wrong!  Perhaps you should reaquaint yourself with the Bard from Stratford upon Avon.
    ''',
    '''a''', False],

    ['''
    What is the primary reason Millennials are unable to buy houses?

    A)Poor economic management and       B)Corporate greed
    policy decision making from the previous generation
    C)Avocados                           D)The free market
    ''','''
    Correct - Poor money management and lack of get up and go is the reason that many in the 'Millennial' generation are unable to afford houses. Other reasons include: cereal cafes, inability to open a can of beans, being a snowflake and not working as hard as the previous generation, apparently.
    ''','''
    Wrong! Back to the Northern Quarter with you. 
    '''
    ,'''c''', False],

    ['''
    Which of the following video game franchises is the brain child of the famous director Hideo Kojima?

    A)Plastic Wrench Liquid              B)Metal Gear Solid

    C)Call of Duty                       D)Shout of Obligation
    ''','''
    Correct - Despite it's convoluted story and awkward name. Metal Gear Solid remains the defining franchise of the stealth genre.
    ''','''
    Snake what happened? Snake? SSSSSSNNNNNNNNAAAAAAAAAAAAAAAAAAKKKKKKKKKKKKKKKKKKEEEEEEEEEE!
    '''
    ,'''b''', False],

    ['''
    Which of the following US Presidents suffered from extreme stage fright?

    A)Alexander Hamilton                 B)Abraham Lincoln

    C)Thomas Jefferson                   D)Ulysses Grant
    ''','''
    Correct - Despite his portrayal in the hit musical 'Hamilton' Thomas Jefferson only gave two speeches in his life and even then audiences had to strain to hear him. This was despite kicking ass as the ambassador to France.
    ''','''
    I'm afraid you will never be president, or in the room where it happens. Thomas Jefferson was the one with stage fright!
    '''
    ,'''c''', False],

    ['''
    Recent research suggests that dinosaurs who once ruled the planet has what kind of skin?

    A)Leathery                           B)Smooth

    C)Furry                              D)Feathery
    ''','''
    Correct - Recent research suggests that dinosaurs, as they were more closely related to birds were feathered. Even the fearsome T-Rex is considered to have had feathers along it's head, neck and tail. The velociraptor was about the size of a chicken and feathered as such. Clever girl...
    ''','''
    You have been eaten by a T-Rex.
    '''
    ,'''d''', False],

    ['''
    Who is England's all time top goal scorer?

    A)  Bobby CHarlton                   B)  Gary Lineker

    C)  Wayne Rooney                     D)  Alan Shearer
    ''','''
    Correct! Wayne Rooney overtook Bobby Charlton's recored of 49 international goals on Tuesday 8th September 2015.
    ''','''
    Wrong! Wayne Rooney overtook Bobby Charlton's recored of 49 international goals on Tuesday 8th September 2015.
    ''',
    'c', False],

    ['''
    Who holds the record for most appearances in the Premier League?

    A)  Ryan Giggs                       B)  Gareth Barry

    C)  James Milner                     D)  David James
    ''','''
    Correct! Gareth Barry holds the record after 653 career Premier League appearances for Aston Villa, Manchester City, Everton & West Brom.
    ''','''
    Wrong! Gareth Barry holds the record after 653 career Premier League appearances for Aston Villa, Manchester City, Everton & West Brom.
    ''',
    'b', False],

    ['''
    Who was the first person in space?

    A)  Yuri gagarin                     B) Buzz Aldrin

    C)  Neil Armstrong                   D) Alan Shepherd
    ''','''
    Correct! Although Neil Armstrong was the first man on the moon and Alan Shepherd was the first American in space, Yuri Gagarin was the first person to go into space.
    ''','''
    Wrong! Although Neil Armstrong was the first man on the moon and Alan Shepherd was the first American in space, Yuri Gagarin was the first person to go into space.
    ''',
    'a', False],

    ['''
    Which nation has won the most World Cups?

    A)  Italy                            B) France

    C)  Germany                          D) Brazil
    ''','''
    Correct! Brazil have won the most World Cups with 5, despite not winning any of the last 4 tournaments.
    ''','''
    Wrong! Brazil have won the most World Cups with 5, despite not winning any of the last 4 tournaments.
    ''',
    'd', False],

    ['''
    Which of these is not a metal?

    A)  Magnesium                        B) Lithium

    C)  Uranium                          D) Nitrogen
    ''','''
    Correct! Nitrogen is the only element that is not a metal.
    ''','''
    Wrong! Nitrogen is the only element that is not a metal.
    ''',
    'd', False],

    ['''
    Who is often called the father of the computer?

    A) Eben Upton                       B)David Montgomery

    C) Charles Babbage                  D) William Shockley
    ''','''
    Correct! 
    ''','''
    Wrong! 
    ''','''c''', False],

    ['''
    Which of these is not a seconday primary colour

    A)RED                               B)YELLOW

    C)CYAN                              D)MAGENTA
    ''','''
    Correct! The primary colours are RED GREEN and BLUE
    and the secondary primaries are MAGENTA CYAN and YELLOW
    ''','''
    Wrong! The primary colours are RED GREEN and BLUE
    and the secondary primaries are MAGENTA CYAN and YELLOW
    ''','''a''', False],

    ['''
    What is the answer to this maths question 2**8

    A)256                               B)64

    C)1024                              D)512
    ''','''
    Correct! 2 x 2 x 2 x 2 x 2 x 2 x 2 x2  =  256
    Two to the power of 8
    ''','''
    Wrong! 2 x 2 x 2 x 2 x 2 x 2 x 2 x2  =  256
    Two to the power of 8
    ''','''a''', False],
    
    ['''
    What is Morrissey the singer with the Smiths middle name

    A)Patrick                           B)Robert

    C)Albert                            D)Marvin
    ''','''
    Correct! Morrisseys middle name is Patrick
    ''','''
    Wrong! 
    ''','''a''', False],

    ['''
    Who is credited with creating the first compiler for a computer programming language

    A)Grace Hopper                      B)Ada Lovelace

    C)Dennis Hopper                     D)Sophie Wilson
    ''','''
    Correct! Grace Brewster Murray Hopper (née Murray December 9, 1906 – January 1, 1992) 
    was an American computer scientist and United States Navy rear admiral.[1] One of the 
    first programmers of the Harvard Mark I computer,
    ''','''
    Wrong! Grace Brewster Murray Hopper (née Murray December 9, 1906 – January 1, 1992) 
    was an American computer scientist and United States Navy rear admiral.[1] One of the 
    first programmers of the Harvard Mark I computer,
    ''','''a''', False],

    ['''
    What is the longest river in the UK?

     A) Thames                          B) Severn

     C) Tyne                            D) Bain
    ''','''
    Correct! The longest river is the Severn, you live another day.
    ''','''
    Wrong! The longest river is the Severn.
    ''','''b''',False],

    ['''
    Which Indian inspired dish is only served in the United Kingdom?

    A) Madras                           B) Chicken Tikka Massala

    C) Vindaloo                         D) Naan bread
    ''','''
    Correct! Chicken Tikka Massala is only served in the UK.
    ''','''
    Wrong! The Indian inspired dish served only in the UK is Chicken Tikka Massala.
    ''','''
    b''',False],

    ['''
    Which mountain is the closest to space?

    A) Space Mountain                   B) Mount Everest
    
    C) Mount Chimborazo                 D) Mount Harpo
    ''','''
    Correct! Mount Chimborazo is indeed the mountain closest to space.
    ''','''
    Wrong! The mountain closest to space is Mount Chimborazo.
    ''','''c''',False],

    ['''
    In January, the Bank of England released a new £20 note with JMW Turner's face on. Who's he?

    A) A famous painter                 B) The Queen's pastry chef
 
    C) The Mayor of London              D) The man who invented the trampoline
    ''','''
    Correct, JMW Turner was indeed a famous painter.
    ''','''
    Wrong! JMW Turner was a famous painter.
    ''','''a''', False],

    ['''
    Which of the following is not a country in Europe?

    A) Albania                          B) Ukraine
   
    C) Estonia                          D) Turkey
    ''','''
    Correct! Turkey is not a country in Europe.
    ''','''
    Wrong! I'm afraid the country not in Europe is Turkey!
    ''','''d''', False]
   ]



# function which asks a question
def question(pos):
    list_of_questions[pos][4]
# for loop prints question on the screen
    for i in list_of_questions[pos][0]:

        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(0.03)

    ans = input('\n\nEnter your answer here :') # get answer from contestant
    ans = ans.lower()
    if ans == list_of_questions[pos][3]:          # NOTE this line matches the correct answer in the question
        for i in list_of_questions[pos][1]: # run if answer is correct
            sys.stdout.write(i)
            sys.stdout.flush()
            sleep(0.03)          
    else:
        for i in list_of_questions[pos][2]:  # run if answer is wrong
            sys.stdout.write(i)
            sys.stdout.flush()
            sleep(0.03)
            


#This will generate the random question
i = len((list_of_questions)*2)
random_q = randint(0, (len(list_of_questions)))
len(list_of_questions)
while(i > 0 and list_of_questions[random_q][4]):
    random_q = randint(0, len(list_of_questions))
    question(random_q)
    i -= 1
    
for i in range(25):
    question(random.randint(0, len(list_of_questions)))


