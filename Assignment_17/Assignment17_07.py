def Star(No):
    for i in range(No):
        for j in range(1,No+1): #row
            print( j,end="  ")  #colunm
        print()


def main():
    Num=int(input("Enter the Number: "))
    Star(Num)
   
if __name__=="__main__":
    main()