import array

my_list = [1,2,3]
my_array = array.array('i', [1, 2, 3, 4]) 
my_tuple = (1,2,3, 'hi')



my_list[0] = 99          # Works
my_array[0] = 99         # Works
# my_tuple[0] = 99       # Error - immutable

print(my_list)
print(my_array)
print(my_tuple)