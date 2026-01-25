def perfect(n):
    sum_of_divisors = 0
    for i in range(1, n):   # Check all numbers less than n
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == n  # True if sum equals number

def main():
    num = int(input("Enter a number: "))

    if perfect(num):
        print(num, "is a Perfect Number")
    else:
        print(num, "is Not a Perfect Number")

if __name__ == "__main__":
    main()
