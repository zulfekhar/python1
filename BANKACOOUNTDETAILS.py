class bankaccount_details:
    def __init__(self,balance= 0):
        self.balance = 0
        print("Deposit And withdarwal machine")

    def deposit(self):
        amount=float(input("enter Depositing amount :" ))
        self.balance += amount
        print("\nAmount Desposited" ,amount )

    def withdarwal(self):
        amount = float(input("Enter withdrawal amount :" ))
        if self.balance >= amount :
            self.balance -= amount 
            print("\nWithdrawn amount" , amount)
        else:
            print("Insufficient balance")

    def available_amount(self):
        print( "Net Availbable amount" , self.balance)

B = bankaccount_details()

B.deposit()
B.withdarwal()
B.available_amount()

