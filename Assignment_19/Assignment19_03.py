from functools import reduce

def main():
    n = int(input("Enter number of elements: "))
    numbers = []

    for i in range(n):
        num = int(input("Enter element: "))
        numbers.append(num)

    # Filter: numbers between 70 and 90
    filtered = list(filter(lambda x: x >= 70 and x <= 90, numbers))

    # Map: increase each number by 10
    mapped = list(map(lambda x: x + 10, filtered))

    # Reduce: product of all numbers
    result = reduce(lambda a, b: a * b, mapped)

    print("Filtered list:", filtered)
    print("Mapped list:", mapped)
    print("Product of numbers:", result)

if __name__ == "__main__":
    main()
