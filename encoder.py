def main():
    choice = '0'
    while choice != '3':
        print_menu()
        choice = input("Please enter an option: ")

        if choice == '1':
            number = input("Please enter your password to encode: ")
            result = encode(number)
            print("Your password has been encoded and stored!\n")
        elif choice == '2':
            answer = decode(result)
            print(f"The encoded password is {result}, and the original password is {answer}.")
            print()
        elif choice == '3':
            break


def print_menu():
    print("Menu")
    print("-------------")
    print('1. Encoder')
    print('2. Decoder')
    print('3. Exit')
    print()


def encode(number):
    encoded_number = ""
    for digit in str(number):
        digit = int(digit)
        encoded_number += str(digit + 3 if digit < 7 else digit - 7)

    return int(encoded_number)


def decode(number):
    decoded_number = ""
    for digit in str(number):
        digit = int(digit)
        decoded_number += str(digit - 3 if digit >= 3 else digit + 7)

    return int(decoded_number)


if __name__ == '__main__':
    main()
