from math import factorial

def print_pascal_triangle_row(row_index):
    for j in range(row_index + 1):
        coefficient = factorial(row_index) // (factorial(j) * factorial(row_index - j))
        print(coefficient, end=" ")
    print()

def print_pascal_triangle(size):
    for i in range(size):
        for _ in range(size - i + 1):
            print(end=" ")

        print_pascal_triangle_row(i)

if __name__ == "__main__":
    x = int(input("Enter the size of Pascal's Triangle: "))
    print_pascal_triangle(x)
