n = input("Please enter a number: ")
try:
 n = int(n)
 print(n)
except ValueError:
 print("Requires a valid integer!")
