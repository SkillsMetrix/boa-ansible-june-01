
from RBI import RBIApp

class SBI(RBIApp):
    initialBalance=100
    def checkBalance(self):
        print (f"SBI is showing Balance in Bank {self.initialBalance}")

    def depositAmount(self,amount):
        self.initialBalance +=amount
        print (f"{amount} is deposited in SBI Bank")
        self.checkBalance()

    def withdrawAmount(self,amount):
        self.initialBalance -=amount
        print (f"{amount} is withdrawn in SBI Bank")
        self.checkBalance()

sbi= SBI()
sbi.depositAmount(1200)
sbi.withdrawAmount(300)
