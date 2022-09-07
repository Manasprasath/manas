def is_perfect_square(num):
    temp = num**(0.5)
    return (temp//1)==temp

print("25 is a valid perfect square")
print(is_perfect_square(25))
print("\n")
print("23 is a valid perfect square")
print(is_perfect_square(23))
