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

    while(i<=10):
        comp = random.choice(list)
        print("Round :",i)
        user = input("Enter you choice :")
        if user =="s":
            comp =="g"
            print("Computer wins")
            print("Computers's choice was : g")
            c +=1
        elif user =="w":
            comp == "s"
            print("Computer wins")
            print("Computers's choice was : s")
            c +=1
        elif user =="g":
            comp=="w"
            print("Computer wins")
            print("Computers's choice was : w")
            c +=1
        else:
            print("You entered Invalid input")
        i +=1
    print("Scoreboard :\n")
    print("You : ",u)
    print("Computer : ",c)
    print("Tie : ",t)
else:
    print("Thankyou , Visit us next time!!")
