def check_numbers(numbers):
    if numbers[0] == numbers[-1]:
        return True
    else:
        return False

list1 = [10, 20, 30, 40, 10]
list2 = [10, 20, 30, 40, 50]

print(check_numbers(list1))
print(check_numbers(list2))

# Output:
# True
# False
