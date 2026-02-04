def main():
    source = input("Enter source file name: ")
    destination = input("Enter destination file name: ")

    try:
        src = open(source, "r")
        data = src.read()
        src.close()

        dest = open(destination, "w")
        dest.write(data)
        dest.close()

        print("File copied successfully.")

    except FileNotFoundError:
        print("Source file does not exist.")


if __name__ == "__main__":
    main()
