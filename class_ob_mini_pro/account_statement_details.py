class AccountStatementDetails:
    def __init__(self, account_holder_name:str,account_number:int,opening_balance:int,):
        self.account_holder_name=account_holder_name
        self.account_number=account_number
        self.opening_balance=opening_balance

    def deposit(self,amount:int)->None:
        self.opening_balance=self.opening_balance+amount
        print(f"Deposited {amount} successfully. New balance is {self.opening_balance}")

    def withdraw(self,amount:int)->None:
        if amount>self.opening_balance:
            print("Insufficient balance. Withdrawal failed.")
        else:
            self.opening_balance=self.opening_balance-amount
            print(f"Withdrew {amount} successfully. New balance is {self.opening_balance}")


    def show_balance(self)->None:
        print(f"Account Holder: {self.account_holder_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.opening_balance}")

accountstatus=AccountStatementDetails("Alam",123456789,1000)
accountstatus.deposit(500)
accountstatus.show_balance()