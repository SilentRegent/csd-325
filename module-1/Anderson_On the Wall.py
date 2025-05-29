"""
Program: 100 Bottles of Beer
Author:Zachary Anderson
Date:5/28/25
Assignment:Module 1.3
Purpose: Prompt the user for a number of beer bottles and display a countdown song that decreases the count by one each time until none are left.

"""
#defines starting point of bottles in function
def countdown(bottles):
    while bottles > 0:
        #when 1 bottle remains the message changes to a single bottle
        if bottles == 1:
            print("1 bottle of beer on the wall, 1 more bottle of beer.")
            print("Take one down and pass it around, no more bottles of beer on the wall.\n")
        else:
            print(f"{bottles} bottles of beer on the wall, {bottles} more bottles of beer.")
            print(f"Take one down and pass it around, {bottles - 1} more {'bottle' if bottles - 1 == 1 else 'bottles'} of beer on the wall.\n")
        #reduces the count by 1 
        bottles -= 1

# Program start
def main():
    try:
        #get input from user for bottle startingg point
        user_bottles = int(input("How many bottles of beer are on the wall? "))
        #validate that number is greater than 0
        if user_bottles < 1:
            print("Please enter a number greater than 0.")
            return
        countdown(user_bottles)
        print("No more bottles of beer!")
    except ValueError:
        print("Please enter a valid number.")

main()