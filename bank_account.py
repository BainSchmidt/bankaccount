bank_data1 = {
    'balance': 500,
    'int_rate': .45,
    'add_amount': 50,
    'sub_amount': 100
}

bank_data2 = {
    'balance': 1200,
    'int_rate': .25,
    'add_amount': 150,
    'sub_amount': 300
}


class BankAccount:
    #BankAccount
    bank_account = []
    def __init__(self, data):
        self.balance = data['balance']
        self.int_rate = data['int_rate']
        self.add_amount = data['add_amount']
        self.sub_amount = data['sub_amount']
        BankAccount.bank_account.append(self)

    # deposit
    def deposit(self):
        self.balance = self.balance + self.add_amount

    # withdraw
    def withdraw(self):
        self.balance = self.balance - self.sub_amount

    def display_account_info(self):
        print(f"Balance: {self.balance}")

    def yield_interest(self):
        self.balance = self.balance * self.int_rate

    @classmethod
    def print_bank_info(cls):
        for bank in cls.bank_account:
            bank.display_account_info()

    @classmethod
    def add_fund(cls):
        for add in cls.bank_account:
            add.deposit()

    @classmethod
    def sub_fund(cls):
        for sub in cls.bank_account:
            sub.withdraw()

    @classmethod
    def int_fund(cls):
        for int in cls.bank_account:
            int.yield_interest()

bank_data1 = {
    'balance': 500,
    'int_rate': .45,
    'add_amount': 50,
    'sub_amount': 100
}

bank_data2 = {
    'balance': 1200,
    'int_rate': .25,
    'add_amount': 150,
    'sub_amount': 300
}


class BankAccount2:
    #BankAccount
    bank_account = []
    def __init__(self, data):
        self.balance = data['balance']
        self.int_rate = data['int_rate']
        self.add_amount = data['add_amount']
        self.sub_amount = data['sub_amount']
        BankAccount2.bank_account.append(self)

    # deposit
    def deposit(self):
        self.balance = self.balance + self.add_amount

    # withdraw
    def withdraw(self):
        self.balance = self.balance - self.sub_amount

    def display_account_info(self):
        print(f"Balance: {self.balance}")

    def yield_interest(self):
        self.balance = self.balance * self.int_rate

    @classmethod
    def print_bank_info(cls):
        for bank in cls.bank_account:
            bank.display_account_info()

    @classmethod
    def add_fund(cls):
        for add in cls.bank_account:
            add.deposit()

    @classmethod
    def sub_fund(cls):
        for sub in cls.bank_account:
            sub.withdraw()

    @classmethod
    def int_fund(cls):
        for int in cls.bank_account:
            int.yield_interest()

bank1 = BankAccount(bank_data1)
bank1.add_fund()
BankAccount.print_bank_info()
bank1.add_fund()
BankAccount.print_bank_info()
bank1.add_fund()
BankAccount.print_bank_info()
bank1.sub_fund()
BankAccount.print_bank_info()
bank1.int_fund()
BankAccount.print_bank_info()

bank2 = BankAccount2(bank_data2)
bank2.add_fund()
BankAccount2.print_bank_info()
bank2.add_fund()
BankAccount2.print_bank_info()
bank2.sub_fund()
BankAccount2.print_bank_info()
bank2.sub_fund()
BankAccount2.print_bank_info()
bank2.sub_fund()
BankAccount2.print_bank_info()
bank2.sub_fund()
BankAccount2.print_bank_info()
bank2.int_fund()
BankAccount2.print_bank_info()