# Program to convert a decimal number to binary number.

def decimalToBinary(num):
    # This function converts decimal number to binary and prints it.
    if num > 1:
        decimalToBinary(num // 2)
    print(num % 2, end='')


# Taking input for Decimal number.
number = int(input("Enter any decimal number: "))

decimalToBinary(number)
