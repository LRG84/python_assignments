#write a program that outputs a table of celsius temperatures from 1-100, in increments of 5
#in addition, the corresponding farenheit temperature should be listed.
#upload to github



for a in range (0,101,5):
    cel_temp = a
    far_temp = cel_temp * (9/5) + 32
    print ('celsius =',cel_temp,'farenheit =',far_temp)

