def string_len(lst):
    return list(filter(lambda s : len(s)>5,lst))

def main():
    
    strings=["Neha","Pragati","Siddhi","Agatsya","Vedant","Nia"]
    Result=string_len(strings)
    print("List of strings having lenth greater than 5 is :",Result)

if __name__=="__main__":
    main()