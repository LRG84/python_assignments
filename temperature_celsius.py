#psuedo code
#enter temperature
#if temp >60 and <90 print "warm"
#if temp >90 print "hot"
#if temp <60 print chilly
#give celsius or farenheit option

temp = input("Are you entering data in Celsius or Farenheit? Type C or F: ")
if temp == "C":
    cel_temp = int (input ("Enter Celsius temperature:_ "))
    cel_temp_conversion = cel_temp * (9/5) + 32
    #cel_temp_conversion is now farenheit
    if cel_temp_conversion > 60 and cel_temp_conversion < 90:
        print("Warm")
    elif cel_temp_conversion > 90:
        print("It's hot, turn on that AC - ASAP!")
    else:
        print("It's chilly, put some more wood on that fireplace!")

else:
    first_temp = int(input ("Enter temperature:_ "))
    if first_temp >60 and first_temp <90:
        print ("Warm")
    elif first_temp >90:
        print ("It's hot, turn on that AC - ASAP!")
    else:
        print ("It's chilly, put some more wood on that fireplace!")