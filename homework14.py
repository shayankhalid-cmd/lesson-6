def calculate_money_due(expenses):
  total_due = sum(expenses)
  return total_due
bills = [55.75, 120.00, 30.50, 45.25]
total_bills = calculate_money_due(bills)
print(f"The total amount due for bills is: ${total_bills:.2f}")
invoice_items = [
    ("Service Fee", 150.00),
    ("Parts", 75.50),
    ("Tax", 15.25)
]
item_costs = [item[1] for item in invoice_items]
invoice_total = calculate_money_due(item_costs)

print("\n--- Invoice Details ---")
for item, cost in invoice_items:
  print(f"{item:<15} ${cost:6.2f}")
print("-----------------------")
print(f"The total invoice amount is: ${invoice_total:.2f}")