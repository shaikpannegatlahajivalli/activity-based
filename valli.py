# Campus Event Financial Planning

venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost: "))
transport = float(input("Enter transport cost: "))
certificate = float(input("Enter certificate cost per person: "))
n = int(input("Enter number of participants: "))
fee = float(input("Enter registration fee per person: "))
sponsor = float(input("Enter sponsorship amount: "))

total = venue + equipment + catering + transport + certificate * n
money = n * fee + sponsor
print("Total Cost:", total)
print("Participant Contribution:", n * fee)
print("Shortfall:", max(0, total - money))
print("Minimum Registrations:", int((venue + equipment + catering + transport - sponsor) / (fee - certificate)) + 1)