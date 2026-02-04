import sys
def main():
    if len(sys.argv) != 2:
        print("Usage: python Filename.py <source_file>")
        sys.exit()

source_file = sys.argv[1]
destination_file = "Demo.txt"

try:
    src=open(source_file, "r")
    data = src.read()
    src.close()

    dest=open(destination_file, "w")
    dest.write(data)
    dest.close()

    print("Contents copied successfully into Demo.txt")

except FileNotFoundError:
    print("Source file does not exist.")

if __name__=="__main__":
    main()
