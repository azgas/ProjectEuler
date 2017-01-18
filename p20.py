def factorial(number):
    if number == 1:
        result = 1
    else:
        result = number * factorial(number - 1)
    return result

def sum(number):
    fact = factorial(number)
    number_in_string = str(fact)
    sum = 0
    for digit in number_in_string:
        sum += int(digit)
    return sum
print(sum(100))