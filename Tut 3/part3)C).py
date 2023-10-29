num_1=int(input("Enter the Bill ampunt : "))
sat=int(input('''Input your review 
1 = Totally satisfied 
2 = Satisfied 
3 =Dissatisfied
='''))
a=num_1*10/100+num_1
b=num_1*15/100+num_1
c=num_1*10/100+num_1
    
if sat== 1:
    print(a)
elif sat == 2:
    print(b)
elif sat==3:
    print(c)
else :
    print("Invalid number")


