# Attendance Recovery Computation

held = int(input("Total classes held: "))
attended = int(input("Classes attended: "))
threshold = float(input("Required attendance %: "))

if held <= 0 or attended < 0 or attended > held:
    print("Invalid attendance details")
else:
    percent = attended / held * 100
    print("Current Attendance:", round(percent, 2), "%")
    future = 0
    while (attended + future) / (held + future) * 100 < threshold:
        future += 1
    print("Consecutive classes required:", future)