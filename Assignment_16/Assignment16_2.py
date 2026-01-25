def chkNum(No):
    if No% 2==0:
        print("Even Number")

    else:
        print("Odd Number")

def main():
    Num=int(input("Enter the Number: ",))
    Result=chkNum(Num)

if __name__=="__main__":
    main()