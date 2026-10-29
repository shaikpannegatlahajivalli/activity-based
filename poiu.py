material = 5000
labour = 2000
wastage = 500
machine = 1000
selling_price = 11000
target = 2000

cost = material + labour + wastage + machine
profit = selling_price - cost

print("Total Cost:", cost)
print("Profit:", profit)

if profit >= target:
    print("Profit Target Achieved")
else:
    print("Profit Target Not Achieved")