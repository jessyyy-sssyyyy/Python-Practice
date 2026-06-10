def calculate(number1, number2):
    product = number1 * number2

    if product <= 1000:
        return product
    else:
        return number1 + number2

result = calculate(20, 30)
print("The result is", result)

result = calculate(40, 30)
print("The result is", result)

#output:
# The result is 600
# The result is 70
