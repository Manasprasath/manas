a=int(input("enter the range:"))
for i in range(1,a+1):
    for j in range(0,a-i+1):
        print(",end=" ")
     c=1
     for j in range(1,i+1):
           print(' ',c,sep=' ',end=' ')
           c=c*(i-j)//j
      print()        
