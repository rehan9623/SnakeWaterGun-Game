import random
'''
 1  for snake
-1 for water
 0  for gun
 '''
computer = random.choice([-1,0,1])
youstr=input("Enter your choice : ")
youDict={"s": 1 , "w": -1 , "g":0 }
reverseDict={1:"Snake", -1:"Water" , 0:"Gun"}
you= youDict[youstr]

#now we have 2 numbers(variables) You and Computer

print(f"You chose {reverseDict[you]} \n Computer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a Draw.")                        #pattern
else: '''                                             
    if(computer == -1 and you == 1):     (computer - you ) = -2
        print("You win!")
    elif(computer == -1 and you == 0):   (computer - you ) = -1
        print("You Lose!")
    elif(computer == 1 and you == -1):   (computer - you ) =  2
        print("You Lose!")
    elif(computer == 1 and you == 0):    (computer - you ) =  1
        print("You Win!")
    elif(computer == 0 and you == -1):   (computer - you ) =  -1
        print("You Win!")  
        print("You Win!")
    elif(computer == 0 and you == 1):    (computer - you ) =  -1
        print("You Win!")
        print("You Lose!")
    else:
        print("Somthing is Wrong.....")
        '''
if((computer - you) == -1 or (computer - you) == 2) :
    print("You Lose!")       
else:
    print("You Win")    