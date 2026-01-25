def CheckNum(No):
    if No>0:
        print("Positive Number")

    elif No<0:
        print("Negative Number")

    else:
        print("Zero")        

def main():
    num=int(input("Enter the Number :"))
    CheckNum(num)
   
if __name__=="__main__":
    main()


