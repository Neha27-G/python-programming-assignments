import os

def main():
    filename=input("Enter the name of the Filename:")

    if os.path.exists(filename):
        print(f"file {filename} exist in current directory")

    else:
        print(f"file {filename} does not exist in current directory")

if __name__=="__main__":
        main()

