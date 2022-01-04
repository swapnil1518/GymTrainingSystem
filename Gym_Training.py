# Health Management System
# 3 clients - Harry, Rohan and Hammad
# 3 files for logging food. 3 files for logging exercise.

# Create a food log file for each client
# Create an exercise log file for each client.
# Ask the user whether they want to log or retrieve client data.
# Write a function that takes the user input of the client's name.
# After the client's name is entered, A message should display "What you want to log. Diet or Exercise"

# Use function
# def getdate():
#   import datetime
#  return datetime.datetime.now()
# The purpose of this function is to give time with every record of food or exercise added in the file.
# Write a function to retrieve exercise or food file records for any client.


import datetime


def getdate():
    return datetime.datetime.now()


def take(k):    # name
    if k == 1:
        c = int(input("Enter 1 for Exercise and 2 for Food"))
        if c == 1:
            value = input("type here\n")  # name of exercise
            with open("Clay-ex.txt", "a") as op:    # a=appending the logs
                op.write(str([str(getdate())]) + ": " + value + "\n")   # time of exercise
            print("Successfully written")
        elif c == 2:
            value = input("type here\n")  # name of food
            with open("Clay-food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")
    elif k == 2:
        c = int(input("Enter 1 for Exercise and 2 for Food"))
        if c == 1:
            value = input("type here\n")
            with open("Sam-ex.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")
        elif c == 2:
            value = input("type here\n")
            with open("Sam-food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")
    elif k == 3:
        c = int(input("Enter 1 for Exercise and 2 for Food"))
        if c == 1:
            value = input("type here\n")
            with open("Tina-ex.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")
        elif c == 2:
            value = input("type here\n")
            with open("Tina-food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(Clay),2(Sam),3(Tina)")


def retrieve(k):
    if k == 1:
        c = int(input("Enter 1 for Exercise and 2 for Food"))
        if c == 1:
            with open("Clay-ex.txt") as op:
                for i in op:
                    print(i, end="")  # end used to place space instead of new line
        elif c == 2:
            with open("Clay-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 2:
        c = int(input("Enter 1 for exercise and 2 for Food"))
        if c == 1:
            with open("Sam-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("Sam-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 3:
        c = int(input("Enter 1 for Exercise and 2 for Food"))
        if c == 1:
            with open("Tina-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("Tina-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (Clay,Sam,Tina)")

print("Health Management System")
a = int(input("enter 1 for LOG and 2 for RETRIEVE the value"))
if a == 1:
    b = int(input("Enter 1 for Clay, 2 for Sam, 3 for Tina"))
    take(b)
else:
    b = int(input("Enter 1 for Clay, 2 for Sam, 3 for Tina"))
    retrieve(b)




