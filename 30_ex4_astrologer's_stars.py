"""
ex4
Pattern Printing
input = integer n
boolean = True or False
take input as 1 or 0 which will be typecasted to boolan
so if True for n = 4 then
*
* *
* * *
* * * *
else False for n = 4 then
* * * *
* * *
* *
*
"""

one = int(input("How many rows you want to print\n"))
two = int(input("Type 1 or 0\n"))
new = bool(two)    #typecasting it to boolean

if new == True:
    for i in range(1,one+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif new == False:
    # for decresing i.e reverse loop
    for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
else:
    print("Invalid Input")