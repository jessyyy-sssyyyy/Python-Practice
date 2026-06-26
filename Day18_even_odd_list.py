list1 = [10, 21, 33, 40, 55]
list2 = [12, 15, 18, 25, 30]

new_list = []

for num in list1:
    if num % 2 != 0:
        new_list.append(num)

for num in list2:
    if num % 2 == 0:
        new_list.append(num)

print("Result List:", new_list)

# Output:
# Result List: [21, 33, 55, 12, 18, 30]
