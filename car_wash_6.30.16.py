# Emulate a car wash by asking user for type of car and type of wash. Give user the options for both.
# Set your prices depending on type of wash and type of car.
# Output should be a print statement that will tell the user what type of wash and car along with the price of the wash (including tax)
# ie format should be something like : “ You have chosen (type of wash) for (type of car), your total will be (price)

print ("Type of car: 1. Sedan, 2. SUV, 3. Van, 4. Limo")
car = input ("Type of car: ")

if car == "1":
    print ("You have chosen sedan.")
    print("Platinum: Clear coat wax - Triple Polish - Rust inhibitor - Hubcaps won't be stolen - Tire shine: $22.99")
    print(
        "Gold: Clear coat wax - Polish foam wax - Rush inhibitor - Hubcaps will be replaced with cheaper ones:  $17.99")
    print(
        "Silver: Exterior and interior wash - Interior vacuum - Windows cleaned - Hand towel drying - Hubcaps painted silver: $23.99")
    type_of_wash = input ("What type of wash would you like? Enter P or G or S. ")
    if type_of_wash == "P" or type_of_wash == "p":
        print ("You have chosen Platinum. Your cost is $22.99 + tax")
        sedan_p = 22.99
        tax = 1.08875
        sedan_p_total = sedan_p * tax
        print ("Your total cost is: $" + str(sedan_p_total) + ".")
    if type_of_wash == "G" or type_of_wash == "g":
        print("You have chosen Gold. Your cost is $17.99 + tax")
        sedan_g = 17.99
        tax = 1.08875
        sedan_g_total = sedan_g * tax
        print("Your total cost is: $" + str(sedan_g_total) + ".")
    if type_of_wash == "S" or type_of_wash == "s":
        print("You have chosen Silver. Your cost is $23.99 + tax")
        sedan_s = 23.99
        tax = 1.08875
        sedan_s_total = sedan_s * tax
        print("Your total cost is: $" + str(sedan_s_total) + ".")

if car == "2":
    print("You have chosen SUV.")
    print("Platinum: Clear coat wax - Triple Polish - Rust inhibitor - Hubcaps won't be stolen - Tire shine: $22.99")
    print(
        "Gold: Clear coat wax - Polish foam wax - Rush inhibitor - Hubcaps will be replaced with cheaper ones:  $17.99")
    print(
        "Silver: Exterior and interior wash - Interior vacuum - Windows cleaned - Hand towel drying - Hubcaps painted silver: $23.99")
    type_of_wash = input("What type of wash would you like? Enter P or G or S. ")
    if type_of_wash == "P" or type_of_wash == "p":
        print("You have chosen Platinum. Your cost is $22.99 + tax")
        suv_p = 22.99
        tax = 1.08875
        suv_p_total = suv_p * tax
        print("Your total cost is: $" + str(suv_p_total) + ".")
    if type_of_wash == "G" or type_of_wash == "g":
        print("You have chosen Gold. Your cost is $17.99 + tax")
        suv_g = 17.99
        tax = 1.08875
        suv_g_total = suv_g * tax
        print("Your total cost is: $" + str(suv_g_total) + ".")
    if type_of_wash == "S" or type_of_wash == "s":
        print("You have chosen Silver. Your cost is $23.99 + tax")
        suv_s = 23.99
        tax = 1.08875
        suv_s_total = suv_s * tax
        print("Your total cost is: $" + str(suv_s_total) + ".")

if car == "3":
    print("You have chosen Van.")
    print("Platinum: Clear coat wax - Triple Polish - Rust inhibitor - Hubcaps won't be stolen - Tire shine: $22.99")
    print(
        "Gold: Clear coat wax - Polish foam wax - Rush inhibitor - Hubcaps will be replaced with cheaper ones:  $17.99")
    print(
        "Silver: Exterior and interior wash - Interior vacuum - Windows cleaned - Hand towel drying - Hubcaps painted silver: $23.99")
    type_of_wash = input("What type of wash would you like? Enter P or G or S. ")
    if type_of_wash == "P" or type_of_wash == "p":
        print("You have chosen Platinum. Your cost is $22.99 + tax")
        van_p = 22.99
        tax = 1.08875
        van_p_total = van_p * tax
        print("Your total cost is: $" + str(van_p_total) + ".")
    if type_of_wash == "G" or type_of_wash == "g":
        print("You have chosen Gold. Your cost is $17.99 + tax")
        van_g = 17.99
        tax = 1.08875
        van_g_total = van_g * tax
        print("Your total cost is: $" + str(van_g_total) + ".")
    if type_of_wash == "S" or type_of_wash == "s":
        print("You have chosen Silver. Your cost is $23.99 + tax")
        van_s = 23.99
        tax = 1.08875
        van_s_total = van_s * tax
        print("Your total cost is: $" + str(van_s_total) + ".")

if car == "4":
    print("You have chosen Limo.")
    print("Platinum: Clear coat wax - Triple Polish - Rust inhibitor - Hubcaps won't be stolen - Tire shine: $22.99")
    print(
        "Gold: Clear coat wax - Polish foam wax - Rush inhibitor - Hubcaps will be replaced with cheaper ones:  $17.99")
    print(
        "Silver: Exterior and interior wash - Interior vacuum - Windows cleaned - Hand towel drying - Hubcaps painted silver: $23.99")
    type_of_wash = input("What type of wash would you like? Enter P or G or S. ")
    if type_of_wash == "P" or type_of_wash == "p":
        print("You have chosen Platinum. Your cost is $22.99 + tax")
        limo_p = 22.99
        tax = 1.08875
        limo_p_total = limo_p * tax
        print("Your total cost is: $" + str(limo_p_total) + ".")
    if type_of_wash == "G" or type_of_wash == "g":
        print("You have chosen Gold. Your cost is $17.99 + tax")
        limo_g = 17.99
        tax = 1.08875
        limo_g_total = limo_g * tax
        print("Your total cost is: $" + str(limo_g_total) + ".")
    if type_of_wash == "S" or type_of_wash == "s":
        print("You have chosen Silver. Your cost is $23.99 + tax")
        limo_s = 23.99
        tax = 1.08875
        limo_s_total = limo_s * tax
        print("Your total cost is: $" + str(limo_s_total) + ".")

print ("Do you want to pay for another car wash?")
another_wash = input ("Enter Y for Yes or N for No.")

while another_wash == ("Y"):


    print ("Thank you for your business. Please come back again!")