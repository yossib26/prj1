num_grid = [
    [1,2,3,4],
    [5,6,7,8],
    [22,26,27,28]
]

print(num_grid[2][2])
print(num_grid[0][0])


# nasted loop
for row in num_grid:
    for col in row:
        print(col)


#print(num_grid)