#!/usr/bin/python3

def pascal_triangle(n):
    """Returns a list of lists representing Pascal's Triangle of n."""
    if n <= 0:
        return []
    
    triangle = [[1]]  # Initialize with the first row
    
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # First element is always 1
        
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        
        new_row.append(1)  # Last element is always 1
        triangle.append(new_row)
    
    return triangle

# Example usage:
n = 5
for row in pascal_triangle(n):
    print(row)

