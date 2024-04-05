class Account():
    def __init__(self,userId,pin,balance=0):
        self.userId = userId
        self.pin = pin 
        self.balance = balance 
        self.transactions = []
    def Deposit(self,amount):
        self.balance = self.balance + amount 
        temp = {"deposit" : amount,"transaction_id":(len(self.transactions)+1)}
        self.transactions.append(temp)
        print("Deposit of amount",amount,"is successfull.")
    def Withdrawl(self,amount):
        if(self.balance>=amount and amount>0):
            self.balance = self.balance-amount 
            withdrawl_temp = {"withdraw" : amount,"transaction_id":(len(self.transactions)+1)}
            self.transactions.append(withdrawl_temp)
            print("Withdrawl of amount :",amount,"is successfull")
            #self.CheckBalance()
        else:
            print("Insufficient balance to withdraw the amount.")
    def Transfer(self,receiever,amount):
        if(self.balance>=amount and amount>0):
            receiever.balance+=amount
            self.balance-=amount
            transaction_temp = {"Transfered to":receiever.userId,"amount" : amount,"transaction_id":(len(self.transactions)+1)}
            self.transactions.append(transaction_temp)
            print(amount,"transfered to",receiever.userId,"is successfull.")
            temp2 = {"Received from":self.userId,"amount":amount,"transaction_id":(len(receiever.transactions)+1)}
            receiever.transactions.append(temp2)
            #self.CheckBalance()
        else:
            print("Insufficient balance to complete transaction")
    def TransactionHistory(self):
        if(len(self.transactions)!=0):
            for i in self.transactions:
                for j in i:
                    print("{} : {},".format(j,i[j],j,i[j]),end = " ")
                print()
        else:
            print("No transactions done")
    def CheckBalance(self):
        print("Current balance : ",self.balance)
    

def makeTransactions(user,user_1,user_2):
    while True:
        print("1.Deposit")
        print("2.Withdrawl")
        print("3.Transfer")
        print("4.Transaction History")
        print("5.Check balance")
        print("6.Exit")
        print("\n\n")
        choice = int(input("Enter choice : "))
        if(choice==1):
            amt = int(input("Enter amount to deposit : "))
            user.Deposit(amt)
        elif(choice==2):
            amt = int(input("Enter amount to withdraw : "))
            user.Withdrawl(amt)
        elif(choice==3):
            receiverId = int(input("Enter receiver Id : "))
            if(receiverId==user_1.userId):
                receiver = user_1
                amt = int(input("Enter amount to transfer : "))
                user.Transfer(receiver,amt)
            if(receiverId ==user_2.userId):
                amt = int(input("Enter amount to transfer : "))
                receiver = user_2
                user.Transfer(receiver,amt)
            else:
                print("Please enter valid receiverId")
        elif(choice==4):
            user.TransactionHistory()
        elif(choice==5):
            user.CheckBalance()
        elif(choice==6):
            print("Logging out user...")
            print("User logged out successfully")
            break
        else:
            print("Enter valid choice")
        

def main():
    user_1 =  Account(1,1234,3000)
    user_2 = Account(2,9876,1000)


    user = None 
    while not user:
        id = int(input("Enter user id : "))
        pin = int(input("Enter pin : "))
        if(id==user_1.userId and pin==user_1.pin):
            user = user_1
            print("\nWelcome user")
            makeTransactions(user,user_1,user_2)
            choice_two = input("Enter Y to login to another account, N to logout")
            if(choice_two=='N'):
                break
            if(choice_two=='Y'):
                user = None
        elif(id==user_2.userId and pin==user_2.pin):
            user = user_2
            print("\nWelcome user")
            makeTransactions(user,user_1,user_2)
            choice_two = input("Enter Y to login to another account, N to logout : ")
            if(choice_two=='N'):
                break
            if(choice_two=='Y'):
                user = None
        else:
            print("Please enter valid user Id and pin")
    
    


if __name__=="__main__":
    main()