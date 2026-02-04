def main():
    filename = input("Enter file name: ")

    try:
        file = open(filename, "r")

        for line in file:
            print(line, end="")

        file.close()

    except FileNotFoundError:
        print("File does not exist.")


if __name__ == "__main__":
    main()
