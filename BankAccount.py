class Bank:
    def __init__(self):
        self.accounts_list = []
        self.table1 = num_generate().num_catalogue[0]
    # def __g-enerate_custom_id(self):
        
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
                self.accounts_list.append(account)
                return f"{account.account_holder} has been added."
            elif action == 'remove' or 'find':
                return f"No data for {account.account_holder}"
        else:
            if action == 'create':
                return f"{account.account_holder} already exist."
            elif action == 'remove':
                self.accounts_list.remove(account)
                return f"{account.account_holder} has been removed."
            elif action == 'find':
                return self.__details(account)
    def __details(self, account):
        return (
                    f"Account name: {account.account_holder}\n"
                    f"Account number: {account.account_num}\n"
                    f"Account name: {account.balance}"
                    )
    def __assign_num(self, account, action):
        if action == 'create':
            num = self.table1[0]
            account.account_num = self.table1[0]
            self.table1.remove(self.table1[0])
            return f"{num}"
        elif action == 'remove':
            num = account.account_num
            self.table1.append(num)
            return f"{num}"
    def create_account(self, account):
        self.__assign_num(account, 'create')
        return self.__action_perform(account, 'create')
    def remove_account(self, account):
        self.__assign_num(account, 'remove')
        return self.__action_perform(account, 'remove')
    def find_account(self, account):
        return self.__action_perform(account, 'find')
    def display_accounts(self):
        for x in self.accounts_list:
            print(f"{self.__details(x)}\n")


class BankAccount:
    def __init__(self, account_holder, balance, bank: Bank):
        self.account_holder = account_holder
        self.balance = balance

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
    def transfer(self, amount, target_account) -> str:
        if self.balance < amount:
            return f"Insuffecient balance to transfer: {amount}"
        target = [x for x in bank.accounts_list if x.account_num == target_account.account_num]
        if target:
            self.balance -= amount
            target_account.deposit(amount)
            return (
                f"Transaction Complete\n"
                f"{amount} had been transfered to {target_account.account_holder}\n"
                f"Current Balance: {self.balance}"
            )
        else:
            return f"No {target_account.account_holder} account"

class num_generate:
    def __init__(self):
        self.combi5 = []
        # contains all tables with different length of digits
        self.num_catalogue = []
        self.combination()
        self.insert_tables(self.combi5)
    def combination(self):
        # for 3125
        for i in range(6):
            for j in range(6):
                for k in range(6):
                    for l in range(6):
                        for m in range(6):
                            self.combi5.append(f"{i}{j}{k}{l}{m}")
    def insert_tables(self, table):
        self.num_catalogue.append(table)
        return self.num_catalogue


bank = Bank()
gene = BankAccount("Gene", 100, bank)
gio = BankAccount("Gene", 100, bank)
nico = BankAccount("Nico", 321, bank)
tet = BankAccount("Tet", 1000, bank)
print(bank.create_account(gene))
print(bank.create_account(nico))
print(bank.create_account(gio))
print(bank.create_account(tet))
print(bank.remove_account(nico))
print(gene.transfer(100, nico))
bank.display_accounts()


# Ensure account_number is unique for each BankAccount created.
# Add error handling for invalid operations, such as withdrawing more than the available balance or attempting to transfer to a non-existent account.