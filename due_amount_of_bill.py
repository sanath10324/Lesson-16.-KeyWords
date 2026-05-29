bill_amount = float(input("Enter your bill amount:"))

paid_amount = float(input("Enter your paid amount:"))

due_amount = bill_amount - paid_amount

if paid_amount < bill_amount:
    print("Customer due amount is:", due_amount)
else:
    print("No due amount")