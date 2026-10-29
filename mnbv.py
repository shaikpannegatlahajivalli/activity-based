entry = int(input("Enter entry hour (0-23): "))
exit = int(input("Enter exit hour (0-23): "))
vehicle = input("Enter vehicle (car/bike): ").lower()

if entry < 0 or entry > 23 or exit < 0 or exit > 23 or entry == exit:
    print("Invalid time")
else:
    hours = (exit - entry) % 24

    if vehicle == "car":
        rate = 50
    elif vehicle == "bike":
        rate = 20
    else:
        rate = 0

    if rate == 0:
        print("Invalid vehicle")
    else:
        fee = hours * rate

        if exit < entry:
            fee = fee + 50

        if fee > 300:
            fee = 300

        print("Parking hours:", hours)
        print("Total parking fee: ", fee)