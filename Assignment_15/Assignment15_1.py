def Square_list(num):
    return list(map(lambda a : a*a ,num))

def main():
    Number=[1,2,3,4,5,6]
    print("Square list of Numbers :",Square_list(Number))

if __name__=="__main__":
    main()