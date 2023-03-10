def main():
    choice = '0'
    while choice != '3':
        print_menu()
        print()
        choice = input("Please enter an option: ")

        if choice == '1':
            unencoded = input("Please enter your password to encode: ")
            encoded = encode(unencoded)
            print("Your password has been encoded and stored!")
        elif choice == '2':
            original = decode(encoded)
            print(f"The encoded password is {unencoded}, and the original password is {original}.")
        elif choice == '3':
            break
    print()


def print_menu():
    print("Menu")
    print("-------------")
    print('1. Encoder')
    print('2. Decoder')
    print('3. Exit')


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
