capacity = 40
passengers = 10
boarding = [5, 10, 8]
alighting = [2, 5, 3]

for i in range(3):
    passengers = passengers + boarding[i] - alighting[i]
    print("Stop", i + 1, "Passengers:", passengers)
    if passengers > capacity:
        print("Capacity exceeded!")