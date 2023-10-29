##x = 45/0
#try:
    #x = int(x)
    #print(x)
#except ZeroDivisionError:
    #print("Cannot divide by zero ")
####n=45/0
#try:
   # print(n)
#except ZeroDivisionError:
   # print("Requires a valid integer!")

try:
    x = 2 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")