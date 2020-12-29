# AnswerBot3000 - Coded by Heno - Answers In An Instant!

import funcinput
import random
import time

#repeat forever loop

while True:

    print('''\n\n---This is the AnswerBot3000---\n\n\n---This was developed by Heno---\n\nBuilt to make hard decisions easy! At the cost of a few clicks of a keyboard,\nhave your decisions made just like that!\n''')
    
    name = funcinput.read_text('Enter your name first for AnswerBot3000:  ')
    
    questionnumwrd = input('\nWhat is your question about? \n1 = Advice on a life decision, 2 = Yes or no, 3 = General life advice:  ')                          

    questionnum=int(questionnumwrd)

#asks person for answer-answer not needed-results=random

    answerdontmatter = funcinput.read_text('\nWhat is your question?:  ')  

    print('\nYour answer is calculating...\n')

    time.sleep(0.5)

    print('...\n')

    time.sleep(0.5)

    print('...\n')

    time.sleep(0.5)

    print('...\n')

    time.sleep(0.5)

    print('...\n')

    time.sleep(0.5)

#yes or no

    if questionnum == 2:

        fortune = random.randint(1,3)

        if fortune == 1:

            print(name, ', my prediction says yes.')
            time.sleep(5)

        if fortune == 2:

            print(name, ', my prediction is off, I am not entirely sure! Maybe ask again?')
            time.sleep(5)

        if fortune ==3:

            print(name, ', sadly, my prediction says no. Maybe its for the better.')
            time.sleep(5)

#advice on life decision

    if questionnum == 1:

        fortune = random.randint(1,3)

        if fortune == 1:

            print(name, ', you have a 50-50 chance of success! Only the worthy are brave enough to risk it for the biscuit!')
            time.sleep(5)
            
    
        if fortune == 2:

            print(name, ', the odds are not in your favor! if I was you, I would not take the risk!')
            time.sleep(5)
            

        if fortune == 3:

            print(name, ', this is not right! It says there is a 100% chance that the odds are in your favor! Take the risk!')
            time.sleep(5)

#general life advice
            
    if questionnum == 3:

        print('I am a mere robot, I do not know much, you should probably go to what is called a therapist', name)

    
