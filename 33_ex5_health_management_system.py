# Health Management System
# 3 clients - Harry , Rohan and Hammad
# Total 6 files
# Write a function that when executed as input client name
# one more function to retrieve excercise or food for any client
def getdate():
    import datetime
    return datetime.datetime.now()

print("WELCOME TO HEALTH MANAGEMENT SYSTEM\n")
print("Enter 1 for Harry , 2 for Rohan , 3 for Hamdan ")
client_id = int(input())
if client_id ==1:
    print("Do you want to Lock or Retrieve ")
    print("Press 1 for Lock and 2 for Retrieve")
    in1 = int(input())
    if in1 == 1:
        print("Do you want to Lock Food or Excersice")
        print("Press 1 for Food and 2 for Excercise")
        in2 = int(input())
        if in2 == 1:
            f1 = open("harry_food.txt", "a")
            print("enter the number of food items you want to enter")
            no_of_food = int(input())
            i = 1
            while (i <= no_of_food):
                print("enter your food item", i)
                food_item = input()
                f1.write(food_item)
                i += 1
        elif in2 == 2:
            ex1 = open("harry_ex.txt", "a")
            print("enter the number of excercises you want to enter")
            no_of_excer = int(input())
            i = 1
            while (i <= no_of_excer):
                print("enter your excercise", i)
                excer_item = input()
                ex1.write(excer_item)
                i += 1
        else:
            print("invalid input")

    elif in1 ==2:
        print("Do you want to Retrieve Food or Excersice")
        print("Press 1 for Food and 2 for Excercise")
        re_in2 = int(input())
        if re_in2 == 1:
            f1 = open("harry_food.txt")
            print(getdate())
            print(f1.readlines())
        elif re_in2 == 2:
            f1 = open("harry_ex.txt")
            print(getdate())
            print(f1.readlines())
        else:
            print("invalid input")
elif client_id == 2 :
    print("Do you want to Lock or Retrieve ")
    print("Press 1 for Lock and 2 for Retrieve")
    in1 = int(input())
    if in1 == 1:
        print("Do you want to Lock Food or Excersice")
        print("Press 1 for Food and 2 for Excercise")
        in2 = int(input())
        if in2 == 1:
            f1 = open("rohan_food.txt", "a")
            print("enter the number of food items you want to enter")
            no_of_food = int(input())
            i = 1
            while (i <= no_of_food):
                print("enter your food item", i)
                food_item = input()
                f1.write(food_item)
                i += 1
        elif in2 == 2:
            ex1 = open("rohan_ex.txt", "a")
            print("enter the number of excercises you want to enter")
            no_of_excer = int(input())
            i = 1
            while (i <= no_of_excer):
                print("enter your excercise", i)
                excer_item = input()
                ex1.write(excer_item)
                i += 1
        else:
            print("invalid input")

    elif in1 ==2:
        print("Do you want to Retrieve Food or Excersice")
        print("Press 1 for Food and 2 for Excercise")
        re_in2 = int(input())
        if re_in2 == 1:
            f1 = open("rohan_food.txt")
            print(getdate())
            print(f1.readlines())
        elif re_in2 == 2:
            f1 = open("rohan_ex.txt")
            print(getdate())
            print(f1.readlines())
        else:
            print("invalid input")

elif client_id == 3 :
    print("Do you want to Lock or Retrieve ")
    print("Press 1 for Lock and 2 for Retrieve")
    in1 = int(input())
    if in1 == 1:
        print("Do you want to Lock Food or Excersice")
        print("Press 1 for Food and 2 for Excercise")
        in2 = int(input())
        if in2 == 1:
            f1 = open("hamdaan_food.txt", "a")
            print("enter the number of food items you want to enter")
            no_of_food = int(input())
            i = 1
            while (i <= no_of_food):
                print("enter your food item", i)
                food_item = input()
                f1.write(food_item)
                i += 1
        elif in2 == 2:
            ex1 = open("hamdaan_ex.txt", "a")
            print("enter the number of excercises you want to enter")
            no_of_excer = int(input())
            i = 1
            while (i <= no_of_excer):
                print("enter your excercise", i)
                excer_item = input()
                ex1.write(excer_item)
                i += 1
        else:
            print("invalid input")

    elif in1 ==2:
        print("Do you want to Retrieve Food or Excersice")
        print("Press 1 for Food and 2 for Excercise")
        re_in2 = int(input())
        if re_in2 == 1:
            f1 = open("hamdaan_food.txt")
            print(getdate())
            print(f1.readlines())
        elif re_in2 == 2:
            f1 = open("hamdaan_ex.txt")
            print(getdate())
            print(f1.readlines())
        else:
            print("invalid input")
else:
    print("Client Id doesnt exist")

