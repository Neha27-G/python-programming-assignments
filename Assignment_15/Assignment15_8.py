def Divisible_list(No):
    return list(filter(lambda a : a % 3==0 and a % 5==0,No ))

def main():
    
    list_num=[3,90,7,100,15,45,50,60,120,88,180]
    Result=Divisible_list(list_num)
    print("List of Numbers Divisible by 3 and 5 are :",Result)

if __name__=="__main__":
    main()