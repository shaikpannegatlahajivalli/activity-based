# Smart Parking Fee Management

entry = int(input("Enter entry hour (0-23): "))
exit = int(input("Enter exit hour (0-23): "))
vehicle = input("Vehicle (car/bike): ").lower()
if not (0 <= entry <= 23 and 0 <= exit <= 23):
    print("Invalid time")
elif vehicle not in ["car", "bike"]:
    print("Invalid vehicle")
else:
    hours = (exit - entry) % 24
    hours = hours if hours > 0 else 24
    rate = 30 if vehicle == "car" else 10
    fee = min(hours * rate, 300)
    if exit < entry:
        fee += 50
    print("Parking hours:", hours)
    print("Total parking fee: Rs.", fee)