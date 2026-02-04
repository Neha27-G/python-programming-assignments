import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python compare.py <file1> <file2>")
        sys.exit()

file1 = sys.argv[1]
file2 = sys.argv[2]

try:
    f1 = open(file1, "r")
    f2 = open(file2, "r")

    data1 = f1.read()
    data2 = f2.read()

    f1.close()
    f2.close()

    if data1 == data2:
        print("Success")
    else:
        print("Failure")

except FileNotFoundError:
    print("One or both files do not exist.")

if __name__=="__main__":
    main()