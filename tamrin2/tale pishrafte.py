def convert_to_base(num, base):
    result = ""
    while num > 0:
        remain = num % base
        result = str(remain) + result
        num //= base
    return result


def calculate_sum_of_divisors(num):
    tmp = 0
    for i in range(1, num + 1):
        if num % i == 0:
            tmp += (num // i)
    return tmp


def main():
    list_1 = []
    check_base = 0

    while True:
        num, base = map(int, input("Enter num and base (space-separated): ").split())

        if num + base == -2:
            if check_base > 0:
                print('Invalid base!')
                exit()
            elif check_base == 0:
                break

        if base < 2 or base >= 10:
            check_base += 1

        sum_of_divisors = calculate_sum_of_divisors(num)
        list_1.append(convert_to_base(sum_of_divisors, base))

    final = sum(int(item) for item in list_1)
    print(final)


if __name__ == "__main__":
    main()
