balance = 1000
transactions = ["deposit 500", "withdraw 200", "withdraw 200", "withdraw 200"]

for t in transactions:
    action, amount = t.split()
    amount = int(amount)

    if action == "deposit":
        balance += amount
    elif action == "withdraw" and amount <= balance:
        balance -= amount
    else:
        print("Invalid transaction!")

print("Final Balance: ₹", balance)

if transactions.count("withdraw 200") >= 3:
    print("Suspicious repeated withdrawals!")