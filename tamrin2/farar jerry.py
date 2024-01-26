def create_map(size):
    return ['.' for _ in range(size)]

def print_map(map_list, size):
    for row in map_list:
        for cell in row:
            print(cell, end=' ')
        print()

def move_left(i):
    return max(i - 1, 0)

def move_right(i, x):
    return min(i + 1, x - 1)

def main():
    x = int(input("Enter the size of the map: "))
    i, j = 0, 0
    map_1 = [create_map(x) for _ in range(1000)]
    map_1[0][0] = '*'

    command = input("Enter commands (L/R/B/END): ")
    while command != "END":
        if command == "L":
            i = move_left(i)
        elif command == "R":
            i = move_right(i, x)
        elif command == "B":
            j += 1
        map_1[j][i] = '*'
        command = input()

    while map in map_1:
        map_1.remove(map)

    print_map(map_1, x)

    if i != x - 1:
        print("There's no way out!")

if __name__ == "__main__":
    main()
