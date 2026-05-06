class FinanceManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def delete_transaction(self, transaction_id):
        self.transactions = [t for t in self.transactions if t.id != transaction_id]

    def get_all_transactions(self):
        return self.transactions

    def get_balance(self):
        balance = 0
        for t in self.transactions:
            if t.transaction_type == "income":
                balance += t.amount
            else:
                balance -= t.amount
        return balance