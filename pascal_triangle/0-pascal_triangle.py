#!/usr/bin/python3
def pascal_triangle(n):
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize Pascal's Triangle with the first row [1]
    triangle = [[1]]

    # Generate the next rows of the triangle
    for i in range(1, n):
        # Start each row with a 1
        row = [1]

        # Fill in the middle values of the row (except for the first and last 1)
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        # End each row with a 1
        row.append(1)

        # Append the row to the triangle
        triangle.append(row)

    return triangle

