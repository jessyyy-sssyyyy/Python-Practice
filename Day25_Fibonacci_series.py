n1 = 0
n2 = 1

print("Fibonacci Series:")

for i in range(15):
    print(n1, end=" ")

    next_num = n1 + n2
    n1 = n2
    n2 = next_num

# Output:
# Fibonacci Series:
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
