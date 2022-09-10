a={'a':'1','b':'2'}
print("dictionary : ",a)
key=input("enter the key")
if key in a.keys():
    print("key exists in the dictionary")
    print("key=",key,"and value+",a[key])
else:
    print("key does not exists")
