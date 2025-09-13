# Task 1
arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

for row in range(len(arr)):
    for col in range(len(arr[row])):
        print(f"Row {row}, Column {col}, Value {arr[row][col]}")

# Task 2

row = 4 
col = 4
new_arr = []

for x in range(0, row):
    new_arr.append([])
    for y in range(0, col):
        new_arr[x].append(pow(x * y, 2))
print(new_arr)