import random
# Define the matrix size
n = 5
coefficient = 4

random.seed(coefficient)
matrix = [[random.randint(1, 100) for j in range(n)] for i in range(n)]
for i in range(n):
    matrix[i][i] = 0

# Print the matrix
print("Cost Matrix:")
for row in matrix:
    print(row)