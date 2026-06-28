income = 45000
tax = 0

if income <= 10000:
    tax = 0
elif income <= 20000:
    tax = (income - 10000) * 0.10
else:
    tax = 10000 * 0.10 + (income - 20000) * 0.20

print("Income Tax =", tax)

# Output:
# Income Tax = 6000.0
