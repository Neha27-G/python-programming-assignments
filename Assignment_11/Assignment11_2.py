def countDigits(n):
    count = 0

    if n == 0:
        return 1

    while n != 0:
        count += 1
        n //= 10   #floor division which removes the numbers after decimal points

    return count


def main():
    n = int(input("Enter a number: "))
    print("Count of digits:", countDigits(n))


if __name__ == "__main__":
    main()

