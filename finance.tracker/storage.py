import json
from models import Transaction

def save_to_json(filename, transactions):
    data = [t.to_dict() for t in transactions]
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def load_from_json(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            return [Transaction.from_dict(item) for item in data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []