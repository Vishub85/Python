def print_table(data):
    if not data:
        print("No data to display.")
        return

    print("|", end="")
    for item in data[0]:
        print(f" {item} |", end="")
    print()
    
    # Print separator
    print("|", end="")
    for _ in data[0]:
        print(" --- |", end="")
    print()
    
    # Print data rows
    for row in data[1:]:
        print("|", end="")
        for item in row:
            print(f" {item} |", end="")
        print()

table_data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "San Francisco"],
    ["Charlie", 35, "London"]
]

print_table(table_data)
