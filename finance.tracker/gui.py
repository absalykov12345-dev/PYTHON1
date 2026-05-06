import tkinter as tk
from tkinter import messagebox
from models import Transaction
from manager import FinanceManager
from storage import save_to_json, load_from_json


class FinanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.root.geometry("700x500")

        self.manager = FinanceManager()
        self.manager.transactions = load_from_json("data.json")

        self.next_id = self.get_next_id()

        self.create_widgets()
        self.update_balance_label()

    def get_next_id(self):
        if not self.manager.transactions:
            return 1
        return max(t.id for t in self.manager.transactions) + 1

    def create_widgets(self):
        title = tk.Label(self.root, text="Personal Finance Tracker", font=("Arial", 18, "bold"))
        title.pack(pady=10)

        self.balance_label = tk.Label(self.root, text="Balance: 0", font=("Arial", 14))
        self.balance_label.pack(pady=10)

        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=20)

        tk.Label(form_frame, text="Amount").grid(row=0, column=0, padx=10, pady=5)
        self.amount_entry = tk.Entry(form_frame)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Category").grid(row=1, column=0, padx=10, pady=5)
        self.category_entry = tk.Entry(form_frame)
        self.category_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Date").grid(row=2, column=0, padx=10, pady=5)
        self.date_entry = tk.Entry(form_frame)
        self.date_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Type").grid(row=3, column=0, padx=10, pady=5)
        self.type_var = tk.StringVar(value="expense")
        type_menu = tk.OptionMenu(form_frame, self.type_var, "income", "expense")
        type_menu.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Description").grid(row=4, column=0, padx=10, pady=5)
        self.description_entry = tk.Entry(form_frame)
        self.description_entry.grid(row=4, column=1, padx=10, pady=5)

        add_button = tk.Button(self.root, text="Add Transaction", command=self.add_transaction)
        add_button.pack(pady=10)

    def add_transaction(self):
        try:
            amount = float(self.amount_entry.get())
            category = self.category_entry.get().strip()
            date = self.date_entry.get().strip()
            transaction_type = self.type_var.get()
            description = self.description_entry.get().strip()

            if category == "" or date == "":
                messagebox.showerror("Error", "Category and date cannot be empty.")
                return

            transaction = Transaction(
                self.next_id,
                amount,
                category,
                date,
                transaction_type,
                description
            )

            self.manager.add_transaction(transaction)
            save_to_json("data.json", self.manager.get_all_transactions())

            self.next_id += 1
            self.update_balance_label()
            self.clear_entries()

            messagebox.showinfo("Success", "Transaction added successfully!")

        except ValueError:
            messagebox.showerror("Error", "Amount must be a number.")

    def update_balance_label(self):
        balance = self.manager.get_balance()
        self.balance_label.config(text=f"Balance: {balance}")

    def clear_entries(self):
        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.type_var.set("expense")


root = tk.Tk()
app = FinanceApp(root)
root.mainloop()