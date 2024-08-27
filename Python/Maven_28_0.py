python
    class Budget:
        def __init__(self):
            self.entries = []

        def add_entry(self, department, amount):
            self.entries.append({"department": department, "amount": amount})

        def compare_with_actual(self, actual_data):
            for entry in self.entries:
                actual = actual_data.get(entry["department"], 0)
                print(f"{entry['department']}: Budsjett: {entry['amount']}, Faktisk: {actual}, Avvik: {entry['amount'] - actual}")

    # Eksempelbruk
    budget = Budget()
    budget.add_entry("IT", 100000)
    budget.add_entry("HR", 50000)

    actual_data = {"IT": 95000, "HR": 55000}
    budget.compare_with_actual(actual_data)