def find_pairs_with_sum(numbers, target):
    num_list = numbers.split()
    dict_1 = {int(item): index for index, item in enumerate(num_list)}
    final_dict = {}

    for i in dict_1.keys():
        tmp = target - i
        if tmp in dict_1 and tmp != i:
            sum1 = dict_1[i] + dict_1[tmp]
            if (tmp, i) not in final_dict:
                final_dict[(i, tmp)] = sum1

    return final_dict


def main():
    numbers = input("Enter a list of numbers (space-separated): ")
    target = int(input("Enter the target sum: "))

    final_dict = find_pairs_with_sum(numbers, target)
    final_result = sorted(final_dict.values())

    if not final_dict:
        print("Not Found!")
    else:
        for k in final_result:
            print(k)


if __name__ == "__main__":
    main()
