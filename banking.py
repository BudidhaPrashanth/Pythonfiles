class banking :
    def __init__(self):
        self.balance =0
        print("welcome to deposite machine !!!")
    def deposite(self):
        amount = float(input("enter amount to be deposited :"))
        self.balance =+ amount
        print("amount deposited :",amount)
    def withdraw(self):
        amount = float(input('enter amount to be withdrawn: '))
        if self.balance > amount:
            self.balance  -= amount
            print("amount withdrawn: ",amount)
        else:
            print("insuffieint balance")
    def display(self):
        print("\nnet available balnce:",self.balance)

person = banking()
person.deposite()
person.withdraw()
person.display()