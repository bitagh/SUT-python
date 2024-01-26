import re

def format_text(input_text):
    input_text = input_text.strip()
    input_text = re.sub(r' +', ' ', input_text)
    input_text = re.sub(r"\\n", '\n', input_text)

    formatted_password = ''
    password_list = list(input_text)
    check = 0
    final_password = []

    for char in password_list:
        if char == '@':
            final_password.append('@')
            check += 1
        elif char == '#' and check > 0:
            check -= 1
        else:
            final_password.append(char)

    formatted_password = ''.join(final_password)
    return formatted_password

def main():
    input_text = input("Enter the text: ")
    formatted_text = format_text(input_text)
    print('Formatted Text:', formatted_text)

if __name__ == "__main__":
    main()
