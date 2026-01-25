def main():
    num = int(input("Enter a number: "))

    binary = bin(num)  # Converts to binary string like '0b101'
    print("Binary equivalent is:", binary[2:])  # Remove '0b'

if __name__ == "__main__":
    main()
