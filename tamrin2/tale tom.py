import math

def process_command(command, numbers):
    if command == 'sum':
        return sum(numbers)
    elif command == 'average':
        return round(sum(numbers) / len(numbers), 2)
    elif command in ['lcd', 'gcd']:
        result = numbers[0]
        for num in numbers[1:]:
            result = result * num // math.gcd(result, num) if command == 'lcd' else math.gcd(result, num)
        return result
    elif command in ['min', 'max']:
        return min(numbers) if command == 'min' else max(numbers)
    else:
        return "Invalid command"

def get_command():
    command = input("Enter a command (sum/average/lcd/gcd/min/max): ").strip().lower()
    if command not in ['sum', 'average', 'lcd', 'gcd', 'min', 'max']:
        print("Invalid command")
        exit()
    return command

def get_numbers():
    numbers = []
    while True:
        line = input("Enter a number (or 'end' to finish): ").strip()
        if line == 'end':
            break
        numbers.append(int(line))
    return numbers

def main():
    command = get_command()
    numbers = get_numbers()
    print(process_command(command, numbers))

if __name__ == "__main__":
    main()
