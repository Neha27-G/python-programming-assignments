def main():
    filename = input("Enter file name: ")
    word = input("Enter word to search: ")

    try:
        file = open(filename, "r")
        content = file.read()
        file.close()

        if word in content:
            print(f'Word "{word}" is found in {filename}')
        else:
            print(f'Word "{word}" is NOT found in {filename}')

    except FileNotFoundError:
        print("File does not exist.")


if __name__ == "__main__":
    main()
