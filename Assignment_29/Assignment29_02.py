def main():

    filename=input("Enter the name of the file: ")

    try:
        fobj=open(filename,"r")
        print("File has open successfully")

        Data=fobj.read()
        print("File contents are :",Data)

    except FileNotFoundError:
        print("File is not available")

    finally:
        print("End of Aplication")
    


if __name__=="__main__":
    main()