def main():
    filename = input("Enter file name: ")

    try:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()

        print("Total number of lines in", filename, ":", len(lines))

    except FileNotFoundError:
        print("File does not exist.")


if __name__ == "__main__":
    main()
