class atm():
    def __init__(self,name,balance,pin) :
        self.name=name
        self.balance=balance
        self.pin=pin
    def checkbalnce(self):
        p=int(input('Enter your pin : '))
        if(p==self.pin):
            print("the balance is"+str(self.balance))
        else:
            print("your pin is incorrect")
    def withdraw(self):
        p=int(input('Enter your pin : '))
        if (p==self.pin):
           amount=int(input('Enter the amount you want to withdraw: '))
           if(amount<=self.balance):
               self.balance=self.balance-amount
               print("your new balance is"+str(self.balance))
           else:
               print("you dont have enough balance")
        else:
                print("your pin is incorrect")

    def deposite(self):
        p=int(input('Enter your pin : '))
        if (p==self.pin):
           amount=int(input('Enter the amount you want to deposite: '))
           self.balance=self.balance+amount
           print("your new balance is"+str(self.balance))
        else:
            print("your pin is incorrect")

            


               
              

costomer1=atm("Uswa",10000,1987)
costomer1.checkbalnce()
costomer1.withdraw()                 
costomer1.deposite()        