lines=int(input("enter number of lines :"))
n_spaces = lines 
for i in range(lines):
    if i <= n_spaces:
        spaces = i
    else:
        spaces = lines - i - 1
    print(" " * spaces+ "*" * 8)
