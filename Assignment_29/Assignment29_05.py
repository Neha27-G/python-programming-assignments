
def main():

    filename = input("Enter file name: ")
    search_str = input("Enter string to search: ")

    try:
        file = open(filename, "r")
        content = file.read()
        file.close()

        count = content.count(search_str)

        print(f'"{search_str}" appears {count} times in {filename}')

    except FileNotFoundError:
        print("File does not exist.")

if __name__=="__main__":
    main()