# Lesson 7
import random
dc = int(input("enter number 1 through 20 representing the diffculty class "))
if (1 <= dc <= 20):
    d20 = random.randrange(1,20)
    print (f"you rolled a {d20}")
    if d20 > dc:
        print ("you rolled a number higher than the dc. You suceed! ")
    elif d20 < dc:
        print ("you rolled a number lower than the dc. You fail :( ")
    elif d20 == dc: 
         print ("you rolled the same number as the dc. It's a tie. ")
else: 
    print ("not a number 1-20, try again")
