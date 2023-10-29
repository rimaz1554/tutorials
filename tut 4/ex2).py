total = 0 # sum of scores
count = 0 # number of scores entered
while  True:
    score=int(input("Enter score, enter -9 to end  :  "))
   
    if score == -9:
        break
    else:
          
          total= total + score
          count=count+1
          print(count)
          print("score = ",score)
    
average = float(total)/count
print("class average is ", average)