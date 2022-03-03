# ex6
"""
snake wins against water
water wins against gun
gun wins against snake
input s for snake , w for water and g for gun
play this game for 10 times using while
display scoreboard as well
"""

import random
chance = 10
u = t = c = 0

print("Welcome to this Game\n")
print("Rules of this game are :")
print("Snake beats Water , Water beats Gun and Gun beats Snake")
print("Press s , w , g for Snake , Water and Gun Respectively")
print("There will be total of 10 rounds , try to beat the Computer!!")
print("Press y to continue or n to exit\n")
cont = input()
if cont =="y":
    print("BATTLE BEGINS\n")
    list = ["s","w","g"]
    i=1

    while(i<=chance):
        comp = random.choice(list)
        print("Round :",i)
        user = input("Enter you choice :")
        if user =="s" and comp =="s" or user=="w" and comp=="w" or user=="g" and comp=="g":
            print("Its a Tie")
            print("Computers's choice was :",comp)
            print()
            t += 1
        elif user =="s" and comp=="w" or user =="w" and comp =="g" or user=="g" and comp=="s":
            print("You win!!!")
            print("Computers's choice was :",comp)
            print()
            u +=1
        else :
            print("Computer wins")
            print("Computers's choice was :",comp)
            print()
            c +=1
        i +=1
    print("Scoreboard :\n")
    print("You : ",u)
    print("Computer : ",c)
    print("Tie : ",t)
    if u>c:
        print("Wohoooo!! , You Won this Game")
    elif c>u:
        print("Sawee :( , You lost Try Again")
    else:
        print("Its a Tie ")
else:
    print("Thankyou , Visit us next time!!")
