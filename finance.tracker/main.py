from models import Transaction
from manager import FinanceManager
from storage import save_to_json, load_from_json

manager = FinanceManager()
manager.transactions = load_from_json("data.json")

t1 = Transaction(1, 5000, "Food", "2026-04-13", "expense", "Lunch")
t2 = Transaction(2, 20000, "Salary", "2026-04-13", "income", "Job")

manager.add_transaction(t1)
manager.add_transaction(t2)

print("Balance:", manager.get_balance())

save_to_json("data.json", manager.get_all_transactions())