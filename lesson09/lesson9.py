# Lesson 9
import random
x = True
while x = True:
    user_input = (input("enter your move: "))
    choices = {1 : 'rock', 2 : 'paper', 3 : 'scissors'}
    ai_move = random.choice(choices)
    if user_input in ('rock', 'paper', 'scissors'):
        if user_input == ai_move :
            print("its a tie! ")
        elif user_input in ('rock'):
            if ai_move in ('paper'):
                print("you lose! ")    
            else:
                print("you win! ")          
        elif user_input in ('paper'):
            if ai_move in ('scissors'):
                print("you lose!")   
            else:
                print("you win!")    
        elif user_input in ('scissors'):
            if ai_move in ('rock'):
                print("you lose! ") 
            else:
                print("you win! ")
           