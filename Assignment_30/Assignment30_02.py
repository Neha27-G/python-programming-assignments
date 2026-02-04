def main():
    filename = input("Enter file name: ")

    try:
        file = open(filename, "r")
        content = file.read()
        file.close()

        words = content.split()
        print("Total number of words in", filename, ":", len(words))

    except FileNotFoundError:
        print("File does not exist.")


if __name__ == "__main__":
    main()
