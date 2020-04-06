from typing import List, Tuple, Any 
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

class Person:
    def __init__(self, name = "default", sname = "default"):
        self.__name = name 
        self.__sname = sname 
        self.__accounts:List[Account] = []
        self.__transaction_id_count = 0

    @property
    def name(self):
        return self.__name 
    @property
    def sname(self):
        return self.__sname 

    @property
    def accounts(self):
        return self.__accounts

    def get_account_by_number(self, number):
        for account in self.__accounts:
            if account.acc_number == number:
                return account

    def __str__(self):
        return r"<Person: {name} {sname}"

    def add_account(self, account):
        self.__accounts.append(account)

    def transfer(self, my_account, my_password, other_person, other_account, amount, show_status = False):
        
        my_account = self.get_account_by_number(my_account) # get self account 
        other_person_account = other_person.get_account_by_number(other_account) # get reciver account 

        if my_account.money >= amount and my_account.can_access(my_password):
            
            other_person_account.add_money(amount)
            my_account.withdraw(amount, my_password)
            self.__transaction_id_count += 1

            if show_status: # possible by json 
                
                transaction_id = str(self.__transaction_id_count)+ \
                    str(my_account.client[:3]).upper() +">"+\
                    other_person_account.client[:3].upper() + \
                    str(datetime.date.today()) + "T" + str(datetime.datetime.now().time())
                
                print()
                print(f"Transaction ID: {transaction_id}")
                print(f"Sender->Receiver: from {my_account.client} to {other_person_account.client}")
                print(f"Accounts: from {my_account.acc_number} to {other_person_account.acc_number}")
                print(f"Amount: {amount}\n")

class Account:
    def __init__(self, a_number:str = "xxx", a_pass:str = "xxx", client:Person = None):
        self.__a_number  = a_number 
        self.__a_pass = generate_password_hash(a_pass) 
        self.__client = client 
        self.__client.add_account(self)
        self.__money = 0 

    @property
    def client(self)->str:
        return f"{self.__client.name} {self.__client.sname}" 

    @property
    def acc_number(self)->str:
        return self.__a_number
        
    def can_access(self, password):
        return check_password_hash(self.__a_pass, password)

    @property 
    def money(self)->float:
        return self.__money

    def add_money(self, amount): # no need password in increase amount of money
            self.__money += amount 

    def withdraw(self, money:float, password:str): # need a password to decrease amount of money 
        if self.__money >= money and self.can_access(password):
            self.__money -= money

#============================= Client ================================================== 

def get_status(persons: List[Person]):
    for person in persons:
        for account in person.accounts:
            print(f"{account.client}: account {account.acc_number} has {account.money}")

def main():
    #clients 
    tarlan = Person("Tarlan", "Omarbayli")
    famil = Person("Famil", "Babayev")

    # accounts
    tarlan_account = Account("123-123-123", "tarlans_first_pass", tarlan)
    tarlan_account2 = Account("321-321-321", "tarlans_second_pass", tarlan) 
    famil_account = Account("333-333-333", "famils_first_pass", famil)

    #add money to accounts
    tarlan_account.add_money(55)
    tarlan_account2.add_money(1000)
    famil_account.add_money(100)


    get_status((tarlan, famil))


    tarlan.transfer("123-123-123", "tarlans_first_pass", famil, "333-333-333", 20, show_status = True)
    famil.transfer("333-333-333", "famils_first_pass", tarlan, "321-321-321", 10, show_status = True)
    tarlan.transfer("321-321-321", "tarlans_second_pass", famil, "333-333-333", 15, show_status = True)
    

    print("=================== after transfer ====================")

    get_status((tarlan, famil))

if __name__ == "__main__":
    main()