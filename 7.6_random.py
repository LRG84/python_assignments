ValidInput=True
while(ValidInput):
    try:
        a=int(input("Enter a number between 1-10:_"))
        if a in range (0,11):
                squared=a*a
                print (a,"squared is ",squared)
                ValidInput=False
        else:
            raise IOError

    except ValueError:
         print("You did not enter a numerical number")
    except IOError:
        print("Your number was not in range 1-10.")
