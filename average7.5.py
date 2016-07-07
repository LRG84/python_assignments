# calculate average set of numbers
# Write a small python program that does the following:
# Calculates the average of a set of numbers.
# Ask the user how many numbers they would like to input.
# Display each number and the average of all the numbers as the output.


def calc_average ():
    counter = int (input('How many numbers would you like to input?_'))
    total = 0
    for a in range (0, counter):
        total = total + int(input('Enter number_ '))
    print('The average of your input is ', total/counter)

calc_average ()

