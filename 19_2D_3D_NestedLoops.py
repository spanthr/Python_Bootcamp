number_grid=[
    [1,2,3],
    [4,5,6],
    [6,7,8],
]
#print(range(len((number_grid)))
print(number_grid[0][2])
print(number_grid[2][2])

for row in number_grid:
    print(row)


print("Now the row and columns")

for row in number_grid:
    for col in row:
        print(col)

