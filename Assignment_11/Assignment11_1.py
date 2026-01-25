def Prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def main():
    n = int(input("Enter a number: "))

    if Prime(n):
        print("Prime Number")
    else:
        print("Not Prime Number")


if __name__ == "__main__":
    main()


