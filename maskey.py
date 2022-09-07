d={'a' : 'm', 'b' : 'a', 'c' : 's', 'd' : 'd'}
print("dictionary : ", d)
key=input("enter the key to check")
if key in d.keys( ):
    print("key is present:")
    print(d[key])
else:
    print("key is not there")
    
    
