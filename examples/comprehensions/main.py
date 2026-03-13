matrix = [
    [1, 2, 3, 0],
    [4, 5, 6, 1],
    [7, 8, 9, 0],
]

matrix2 = []
for row in matrix:
    new_row = []
    for item in row:
        new_row.append(item * 2)
    matrix2.append(new_row)

print(matrix2)

matrix3 = [[item * 2 for item in row] for row in matrix]
print(matrix3)
