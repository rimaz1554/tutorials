hidden=6
while True:
     try:
        value=int(input("Enter a value between 2 to 20 :    "))
        if value!=6:
            print("is not correct")
            if value>hidden:
                print(value,"The value is higher than the hidden value")
            else:
                print("The value is lower than the hidden value")
        else:
            print("value is correct")
            break       
     except ValueError:
         print("Invalid input try again")
         