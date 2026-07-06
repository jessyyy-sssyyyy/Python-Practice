list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

common_elements = list(set(list1) & set(list2))

print("Common Elements:", common_elements)

# Output:
# Common Elements: [30, 40, 50]
