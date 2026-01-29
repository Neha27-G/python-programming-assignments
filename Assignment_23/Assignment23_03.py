class Numbers:

    def __init__(self):
        self.Value=int(input("Enter the numbers :"))

    def ChkPrime(self):
        if self.Value<=1:
            return False
    
        for i in range(2,int(self.Value/2)+1):
            if self.Value% i==0:
                return False
            
        return True
    
    def Factors(self):
        print("Factors are:")
        for i in range(1,self.Value+1):
            if self.Value% i==0:
                print(i, end=" ")
        print()


    def SumFactors(self):
        total=0
        for i in range(1,self.Value):
            if self.Value% i==0:
                total+=i
        return total
    
    def ChkPerfect(self):
        if self.SumFactors()==self.Value:
             return True
        else:
            return False
        
obj1=Numbers()
obj2=Numbers()

print("Is Prime :",obj1.ChkPrime())
obj1.Factors()
print("Is Perfect :",obj1.ChkPerfect())
print("------------------------------------")

print("Is Prime :",obj2.ChkPrime())
obj2.Factors()
print("Is Perfect :",obj2.ChkPerfect())
print("------------------------------------")