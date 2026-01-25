def Count_of_Even(Num):
    return len(list(filter(lambda a : a%2==0,Num)))

def main():
    
    Numbers=[1,4,6,3,6,2,1,7,9,8]
    Result=Count_of_Even(Numbers)
    print("Count of Even Number is:",Result)

if __name__=="__main__":
    main()