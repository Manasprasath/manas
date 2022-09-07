def factorial(num):
    return 1 if (num==1 or num==0) else num * factorial(num-1);
number = 6
print("The factorial of",number,"is",factorial(number))
