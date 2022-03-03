# Ex3
n = 18
# no of guesses 9
# print no.of guesses left
# game over
# no.of guesses he took to finish
tot=9
i = 1
while(i<=9):
    inp = int(input("enter your number\n"))
    if inp>n :
        print("greater than the number\n")
    elif inp<n:
        print("lesser than the number\n")
    else:
        print("number found ,it is" , inp)
        print("guesses you took : ",i)
        break
    print("no.of guesses left are" ,tot-i )
    i = i + 1
if i>9:
    print("GAME OVER")



