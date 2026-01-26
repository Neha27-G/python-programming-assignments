from functools import reduce

def main():
    n = int(input("Enter number of elements: "))
    numbers = []

    for i in range(n):
        num = int(input("Enter element: "))
        numbers.append(num)

   
    filtered = list(filter(lambda x: x%2==0, numbers))

    mapped = list(map(lambda x: x**2, filtered))

    result = reduce(lambda a, b: a + b, mapped)

    print("Filtered list:", filtered)
    print("Mapped list:", mapped)
    print("Addition of numbers:", result)

if __name__ == "__main__":
    main()
