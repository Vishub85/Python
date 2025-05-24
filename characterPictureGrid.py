#character printing
char = input("Enter a character to display in the pattern: ")

grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', char, char, '.', '.', '.'],
    [char, char, char, char, '.', '.'],
    [char, char, char, char, char, '.'],
    ['.', char, char, char, char, char],
    [char, char, char, char, char, '.'],
    [char, char, char, char, '.', '.'],
    ['.', char, char, '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']
]

for y in range(len(grid[0])):
    for x in range(len(grid)):
        print(grid[x][y], end=' ')
    print()
