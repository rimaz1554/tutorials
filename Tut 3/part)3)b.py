num_1=int(input("Enter the value : "))
op=int(input('''for operators :
To Add - 1 :
To substract - 2  :  
To  10 multiply -  3 : 
To divide - 4 : 
='''))
num_2=int(input("Enter the value : " ))
a=num_1+num_2
b=num_1-num_2
c=num_1*num_2
d=num_1/num_2
if op== 1:
    print(a)
elif op == 2:
    print(b)
elif op==3:
    print(c)
else :
    print(d)

