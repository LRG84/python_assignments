
#psuedo code
#enter temperature
#if temp >60 and <90 print "warm"
#if temp >90 print "hot"
#if temp <60 print chilly


first_temp = int(input ("Enter temperature:_ "))
if first_temp >60 and first_temp <90:
    print ("Warm")
elif first_temp >90:
    print ("It's hot, turn on that AC - ASAP!")
else:
    print ("It's chilly, put some more wood on that fireplace!")


