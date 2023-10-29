hidden=6
while True:
     try:
        value=int(input("Enter a value between 2 to 20 :    "))
        if value!=6:
            print("is not correct")
        else:
            print(value,"is correct")
     except ValueError:
         print("Invalid input try again")
