# PROJECT 3 – RAILWAY FARE AND RESERVATION CALCULATOR

## About the Project
The Railway Fare and Reservation Calculator project is designed to compute ticket fares for multiple passengers based on travel distance slabs, coach class multipliers, age-based concessions, and reservation charges. It also calculates the cancellation penalty and refundable amount for the booking.

## Technologies Used
- **Python** – Used to implement the railway fare and reservation calculator.
- **Lists & Tuples** – Used to store passenger ticket details for receipt display.
- **Loops** – Used to process fare calculation for each passenger.
- **Conditional Statements** – Used to apply distance slabs, class multipliers, and age concessions.
- **Arithmetic Operators** – Used to compute fares, reservation fees, and cancellation refunds.

## Main Features
- Accepts travel distance, travel class (`SL`, `3AC`, `2AC`), and passenger count.
- Computes base fare across distance slabs (`<=100 km`, `101–500 km`, `>500 km`).
- Applies class multipliers (`1.0x` for `SL`, `2.2x` for `3AC`, `3.0x` for `2AC`).
- Grants free tickets for children under 5 and a 40% fare discount for seniors (`>= 60`).
- Adds a Rs. 40 reservation fee per payable passenger and shows cancellation details.

## Algorithm
1. Start the program.
2. Read travel distance, travel class, and number of passengers.
3. Validate that distance and passenger count are greater than zero.
4. Calculate base fare using the distance slabs and multiply by the class factor.
5. Loop through each passenger to read name and age.
6. Apply child exemption (`age < 5`), senior concession (`age >= 60`), or adult fare, plus Rs. 40 fee.
7. Accumulate total payable fare and store each passenger's summary.
8. Display the reservation receipt along with 25% cancellation penalty and 75% refund.
9. Stop the program.

## Sample Output
Enter travel distance (km): 300
Enter class (SL / 3AC / 2AC): 3AC
Enter number of passengers: 3

Passenger 1:
  Name: Ananya
  Age: 28

Passenger 2:
  Name: Raghav
  Age: 65

Passenger 3:
  Name: Aarav
  Age: 3

----- RAILWAY RESERVATION RECEIPT -----
Ananya (Age 28 - Adult): Rs. 920.0
Raghav (Age 65 - Senior (40% Off)): Rs. 568.0
Aarav (Age 3 - Child (Free)): Rs. 0.0
---------------------------------------
Total Payable Fare      : Rs. 1488.00
Cancellation Penalty    : Rs. 372.00
Refund on Cancellation  : Rs. 1116.00

## Conclusion
This project models multi-passenger railway ticket pricing with concessions and cancellation estimates. It demonstrates Python concepts such as lists, tuples, loops, conditional statements, and arithmetic operations.
