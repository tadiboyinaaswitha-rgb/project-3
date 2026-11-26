distance = float(input("Enter travel distance (km): "))
travel_class = input("Enter class (SL / 3AC / 2AC): ").upper()
n = int(input("Enter number of passengers: "))

if distance <= 0 or n <= 0:
    print("Invalid distance or passenger count.")
else:
    if distance <= 100:
        base = distance * 1.0
    elif distance <= 500:
        base = 100.0 + (distance - 100) * 1.5
    else:
        base = 100.0 + 600.0 + (distance - 500) * 2.0

    if travel_class == "3AC":
        mult = 2.2
    elif travel_class == "2AC":
        mult = 3.0
    else:
        mult = 1.0

    class_fare = base * mult
    total_fare = 0.0
    passengers = []

    for i in range(n):
        print(f"\nPassenger {i + 1}:")
        name = input("  Name: ")
        age = int(input("  Age: "))
        if age < 5:
            fare = 0.0
            cat = "Child (Free)"
        elif age >= 60:
            fare = (class_fare * 0.60) + 40.0
            cat = "Senior (40% Off)"
        else:
            fare = class_fare + 40.0
            cat = "Adult"
        total_fare += fare
        passengers.append((name, age, cat, round(fare, 2)))

    print("\n----- RAILWAY RESERVATION RECEIPT -----")
    for p in passengers:
        print(f"{p[0]} (Age {p[1]} - {p[2]}): Rs. {p[3]}")
    print("---------------------------------------")
    print(f"Total Payable Fare      : Rs. {total_fare:.2f}")
    print(f"Cancellation Penalty    : Rs. {total_fare * 0.25:.2f}")
    print(f"Refund on Cancellation  : Rs. {total_fare * 0.75:.2f}")
