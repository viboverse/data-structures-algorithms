list_1 = [1, 2, 3, 4, 5]
list_2 = [5, 4, 3, 2, 10]
list_3 = [None, 'a', 'b', 'c', 'd']


def combine_lists(a, b, c):
   return  a + b + c


test = combine_lists(list_1,list_2, list_3)
print(test)