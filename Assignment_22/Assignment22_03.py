class Arithmetic:

    def __init__(self):
        self.Value1=0
        self.Value2=0

    def Accept(self):
        self.Value1=int(input("Enter the Value1:"))
        self.Value2=int(input("Enter the Value2:"))

    def Addition(self):
        print("Addition is :",self.Value1+self.Value2)

    def Substraction(self):
        print("Substraction is :",self.Value1-self.Value2)

    def Multiplication(self):
        print("Multiplication is :",self.Value1*self.Value2)

    def Division(self):
        if self.Value2==0:
            print("Division is : Cannot Division by Zero")
        else:
            print("Division is :",self.Value1/self.Value2)


obj1=Arithmetic()

obj1.Accept()
obj1.Addition()
obj1.Substraction()
obj1.Multiplication()
obj1.Division()