# Given a set of numbers, create a program that returns the largest and smallest number in the set.
# Accepts X amount of numbers from a user.
# Store each value in a list.
# Create one or more functions which return the maximum number in the list.
# Create one or  more functions which return the smallest number in the list.
# Upload your code to GitHub.

#ask the user for the numbers they want to add. Make it determined by what they want.
#array is list you're storing numbers in
array=[]

def maximum(input_list):
    maxi = input_list[0]
    for b in input_list:
        if b>maxi:
            maxi=b
        return maxi

def minimum(input_list):
    mini = input_list[0]
    for d in input_list:
        if d < mini:
            mini = d
    return mini

counter = True
while counter == True:
    number = int(input("Please enter a number: "))
    array.append(number)
    end_loop = input("Would you like to continue? [Y/N]")
    if end_loop == "N" or end_loop == "n":
        counter = False
print (minimum(array), maximum(array))
#Check for max
for a in array:
    checker = a

