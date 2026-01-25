def SumDigits(n):
    sum= 0
    while n > 0:
        sum+= n % 10
        n //= 10
    return sum


def main():
    n = int(input("Enter a number: "))
    print("Sum of digits:", SumDigits(n))


if __name__ == "__main__":
    main()


