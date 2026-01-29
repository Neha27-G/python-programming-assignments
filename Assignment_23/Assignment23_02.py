class BankAccount:
   ROI=10.5

   def __init__(self,Name,Amount):
      self.Name=Name
      self.Amount=Amount

   def Display(self):
      print("Account Holder Name:",self.Name)
      print("Current Balance:",self.Amount)

   def Deposit(self):
      amt=float(input("Enter the Amount to Deposit :"))
      self.Amount +=amt
      print("Amount is Deposited")

   def Withdraw(self):
      amt=float(input("Enter the Amount to Withraw :"))

      if amt<= self.Amount:
         self.Amount -=amt
         print("Amount withdraw successfully")
      else:
         print("Insufficient Balance")
      
   def CalculateInterest(self):
      interest=(self.Amount*BankAccount.ROI)/100
      return interest
      
obj1=BankAccount("Neha",5000)
obj2=BankAccount("Amit",10000)

obj1.Display()
obj1.Deposit()
obj1.Withdraw()

print("Interest :",obj1.CalculateInterest())
print("------------------------------------------")

obj2.Display()
obj2.Deposit()
obj2.Withdraw()

print("Interest :",obj2.CalculateInterest())


