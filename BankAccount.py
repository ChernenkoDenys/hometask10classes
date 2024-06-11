# Розробіть клас BankAccount для представлення банківського рахунку. 
# Додайте методи для зняття та поповнення коштів на рахунку. 
# Використовуйте магічний метод __str__ для виведення інформації про рахунок.

class BankAccount:
    
    def __init__(self, money):
        self.check_money_correctness(money)
        self.__money = money
    
    @property
    def money(self):
        return self.__money
    
    @money.setter
    def money(self, money):
        self.__money = money
    
    def withdraw(self, money):
        self.check_money_correctness(money)
        if money > self.__money:
            raise ValueError("Cannot withdraw more than on")
        self.__money -= money
    
    def topup(self,money):
        self.check_money_correctness(money)
        self.__money += money
    
    @staticmethod
    def check_money_correctness(money):
        if not isinstance(money, int):
            raise TypeError("Money must be only integer!")
        elif money < 0:
            raise ValueError("Money cannot be negative numer")
        
    
    def __str__(self):
        return f"Your account balance is {self.__money}"


account = BankAccount(100)
account.withdraw(50)
account.topup(200)
print(account)  
