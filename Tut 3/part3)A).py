x =int(input("Enter 1 if you want to convert celcius to farenheit , Enter 2 if you want to convert  farenheit to celcius :  " ))
y =int(input("Enter the value : "))
c_s=(y * 1.8) + 32
s_c=(y - 32) / 1.8
if x == 1:
    print(c_s,'  farenheits')
elif x == 2:
    print(s_c,'  celcius')
else:
    print("value is not valid")
