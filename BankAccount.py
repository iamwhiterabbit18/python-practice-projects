class NumGenerate:
    def __init__(self):
        self.available_numbers = list(range(1000, 6000))

    def get_next_num(self):
        if self.available_numbers:
            return self.available_numbers.pop(0)
        else:
            raise Exception("No more account numbers available!")
    def return_num(self, num):
        if num not in self.available_numbers:
            self.available_numbers.append(num)
            self.available_numbers.sort()

class Bank:
    def __init__(self):
        self.accounts_list = []
        self.num_generator = NumGenerate()
        self.name = "Genesis Bank"
    def __str__(self):
        return f"{self.name}"
        
    def __checkAccount(self, account):
        target = [x for x in self.accounts_list if account == x]
        if target:
            return target
        else:
            return False
    def __action_perform(self, account, action):
        checked = self.__checkAccount(account)
        if not checked:
            if action == 'create':
                account.account_num = self.num_generator.get_next_num()
                self.accounts_list.append(account)
                return f"{account.account_holder} has been added."
            elif action == 'remove' or 'find':
                return f"No data for {account.account_holder}"
        else:
            if action == 'create':
                return f"{account.account_holder} already exist."
            elif action == 'remove':
                self.num_generator.return_num(account.account_num)
                self.accounts_list.remove(account)
                return f"{account.account_holder} has been removed."
            elif action == 'find':
                return self.__details(account)
    def create_account(self, account):
        return self.__action_perform(account, 'create')
    def remove_account(self, account):
        return self.__action_perform(account, 'remove')
    def find_account(self, account):
        return self.__action_perform(account, 'find')
    def transfer(self, amount, source_account, target_account) -> str:
        if amount <= 0:
            return f"There must be a certain amount."
        if source_account.balance < amount:
            return f"Insuffecient balance to transfer: {amount} from {source_account.account_holder}"
        
        source_account.balance -= amount
        target_account.balance += amount
        return (
            f"Transferred {amount} from {source_account.account_holder} to {target_account.account_holder}.\n"
            f"Source Account Balance: {source_account.balance}\n"
            f"Target Account Balance: {target_account.balance}"
        )
    def display_accounts(self):
        for x in self.accounts_list:
            print(f"{x}\n")

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def __str__(self):
        return (
                    f"Account name: {self.account_holder}\n"
                    f"Account number: {self.account_num}\n"
                    f"Account name: {self.balance}"
                    )
    # def __repr__(self):
    #     return (
    #                 f"BankAccount(account_holder='{self.account_holder}', balance='{self.balance}')")

    def deposit(self, amount) -> str:
        if(amount <= 0):
            return f"There must be a certain amount."
        self.balance += amount
        return (
            f"{amount} deposited successful.\n"
            f"Current Balance: {self.balance}"
        )
    def withdraw(self, amount) -> str:
        if(amount > self.balance):
            return f"You don't have enough balance."
        self.balance -= amount
        return (
            f"{amount} withraw successful.\n"
            f"Current Balance: {self.balance}"
        )
    def check_balance(self) -> str:
        return f"Current Balance: {self.balance}"
bank = Bank()
gene = BankAccount("Gene", 100)
gio = BankAccount("Gene", 100)
nico = BankAccount("Nico", 321)
tet = BankAccount("Tet", 1000)

bank.create_account(gene)
bank.create_account(gio)
bank.create_account(gio)
bank.transfer(100, gene, gio)
bank.display_accounts()