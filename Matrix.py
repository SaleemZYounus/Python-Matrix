
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
print(matrix[2][2])    # 9 

matrix[2][2] = 21     #change

print(matrix[2][2])    # 21 

print('listing all values by row then column')
for row in matrix: #iterating through each row
    for item in row:
        print(item)