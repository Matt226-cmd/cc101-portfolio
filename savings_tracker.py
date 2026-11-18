# savings.py
days = 0
total = 0.0

while True:
    amount = float(input("Enter amount saved today (0 to stop): "))
    if amount == 0:
        break
    days += 1
    total += amount

print(f"Number of days: {days}")
print(f"Total saved: PHP {total:,.2f}")