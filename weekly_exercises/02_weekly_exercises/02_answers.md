# 02_weekly_exercises

### 02-01. Command Line Arguments

```python
import sys

args = sys.argv[1:]

result = ','.join(args)

print(result)
```

### 02-02. Combine Multiple Lists

```python
list_1 = [1, 2, 3, 4, 5]
list_2 = [5, 4, 3, 2, 10]
list_3 = [None, 'a', 'b', 'c', 'd']


def combine_lists(a, b, c):
   return  a + b + c


test = combine_lists(list_1,list_2, list_3)
print(test)

```

### 02-03. Compare different Arrays

```python
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
```
