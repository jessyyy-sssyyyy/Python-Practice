numbers = [10, 25, 3, 48, 17, 6]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest number:", largest)
print("Smallest number:", smallest)

# Output:
# Largest number: 48
# Smallest number: 3
