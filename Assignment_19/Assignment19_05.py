from functools import reduce

def CheckPrime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def main():
    n = int(input("Enter number of elements: "))
    numbers = []

    for i in range(n):
        num = int(input("Enter element: "))
        numbers.append(num)

   
    filtered = list(filter(lambda x:CheckPrime(x), numbers))

    mapped = list(map(lambda x: x*2, filtered))

    result = reduce(lambda a, b: a if a>b else b, mapped)

    print("Prime Numbers:", filtered)
    print("After Multiplcation by 2:", mapped)
    print("Maximum Number:", result)

if __name__ == "__main__":
    main()
