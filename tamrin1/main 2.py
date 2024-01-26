def count_different_bits(a, b):
    xor_result = a ^ b
    count_bits = bin(xor_result).count('1')
    print(count_bits)

def main():
    a = int(input("Enter the first integer: "))
    b = int(input("Enter the second integer: "))
    count_different_bits(a, b)

if __name__ == "__main__":
    main()
