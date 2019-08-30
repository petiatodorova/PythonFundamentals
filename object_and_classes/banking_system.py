class BankAccount:
    def __init__(self, name, bank, balance):
        self.name = name
        self.bank = bank
        self.balance = balance


line = input().split(" | ")

list_accounts = []

while not line[0] == "end":
    bank = line[0]
    accountName = line[1]
    accountBalance = float(line[2])
    current_account = BankAccount(name=accountName, bank=bank, balance=accountBalance)
    list_accounts.append(current_account)
    line = input().split(" | ")

for account in sorted(list_accounts, key=lambda acc: (-acc.balance, len(acc.bank))):
    print(f"{account.name} -> {account.balance:.2f} ({account.bank})")