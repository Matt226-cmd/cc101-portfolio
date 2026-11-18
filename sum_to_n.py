# sum_to_n.py
n = int(input("Enter a positive whole number: "))
total = 0

for i in range(1, n + 1):
    total += i

print(f"Sum from 1 to {n} is {total}.")