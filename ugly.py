def maxdivide(a,b):
    while a % b==0:
        a=a/b
    return a
def isugly(no):
    no = maxdivide(no,2)
    no = maxdivide(no,3)
    no= maxdivide(no,5)
    return 1 if no == 1 else 0
def getnthuglyno(n):
    i=1
    count =1
    while n > count:
        i += 1
        if isugly(i):
            count+=1
    return i
no = getnthuglyno(int(input("enter the no"))
print(" ugly no is",no)
