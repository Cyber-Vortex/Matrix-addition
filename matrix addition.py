# Program to add two 2x2 matrices
# Matrix A config
matrix_A = [
    [1, 2],
    [3, 4]
]

# Matrix B config
matrix_B = [
    [5, 6],
    [7, 8]
]

# Result matrix initialization (2x2 with zeros)
result = [
    [0, 0],
    [0, 0]
]

# Outer loop for rows
for i in range(2):
    # Inner loop for columns
    for j in range(2):
        result[i][j] = matrix_A[i][j] + matrix_B[i][j]

print("Resultant Matrix after Addition:")
for row in result:
    print(row)
