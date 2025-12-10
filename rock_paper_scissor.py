import random
computer = random.choice([1, -1, 0])
youstr = input("Enter your choice: ")

youDict = {"r":1, "p":-1, "s":0}
reverseDict = {1:"rock", -1:"paper", 0:"scissor"}

you = youDict[youstr]

print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if computer == you:
    print("it's a draw")

else:
    if(computer == 1 and you == -1):
        print("you win")
    
    
    elif(computer==1 and you==0):
       print("you lose!")

    elif(computer==-1 and you==1):
       print("you lose!") 

    elif(computer==-1 and you==0): 
       print("you winn!")

    elif(computer==0 and you==-1):
       print("you lose")

    elif(computer==0 and you==1):
       print("you win!")

    else:
       print("something went wrong!!")