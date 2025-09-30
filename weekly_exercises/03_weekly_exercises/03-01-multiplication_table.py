def generate_multiplication_table(n):
    """
    Creates a 2D list representing a multiplication table of size n x n.
    """
    table = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        table.append(row)
    return table

def print_multiplication_table(n):
    """
    Generates and prints a formatted multiplication table.
    """
    table = generate_multiplication_table(n)
    
    # Print the table with proper formatting
    for row in table:
        for value in row:
            print(f"{value:4}", end="") 
        print() 

# Example usage
n = 10
print(f"Multiplication table for n = {n}:")
print_multiplication_table(n)