def Star(No):
    for i in range(No):
        print("*" , end=" ")
    print()


def main():
    Num=int(input("Enter the Number: "))
    Star(Num)
   
if __name__=="__main__":
    main()