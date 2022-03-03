# ex2
# design a calculator which will correctly solve all problems except following one :
# 45*3 = 555 , 56 + 9 = 77 , 56/6 = 4
# your program should take operator as input and opearand as well

print("Enter the two numbers")
num1 = int(input())
num2 = int(input())
print("enter the operator you want to perform")
op = input()

if num1 == 45 and num2 == 3 and op == '*':
    ans = 555
elif num1 == 56 and num2 == 9 and op == '+':
    ans = 77
elif num1 == 56 and num2 == 6 and op == '/':
    ans = 4
elif op == '+':
    ans = (num1 + num2)
elif op == '-':
    ans = (num1 - num2)
elif op == '*':
    ans = (num1 * num2)
elif op == '/':
    ans = (num1 / num2)
else:
    print("please choose a valid input")


print(ans)
