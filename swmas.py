def swap(my_list):
    size_of_list=len(my_list)

    temp=my_list[0]
    my_list[0]=my_list[size_of_list-1]
    my_list[size_of_list-1]=temp
    return my_list
my_list=[34,56,72]
print(my_list)
print(swap(my_list))
