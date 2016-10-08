dictionary = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight',
              '9': 'nine',
              '10': 'ten',
              '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen', '16': 'sixteen',
              '17': 'seventeen',
              '18': 'eighteen', '19': 'nineteen', '20': 'twenty', '30': 'thirty', '40': 'forty', '50': 'fifty',
              '60': 'sixty',
              '70': 'seventy',
              '80': 'eighty', '90': 'ninety'}


def below_ten(number):
    name = dictionary[number]
    return name


def below_hundred(number):
    tens = number[0] + '0'
    if number[0] == '1':
        name = dictionary[number]
    else:
        if number[1] != '0':
            name = dictionary[tens] + below_ten(number[1])
        else:
            name = dictionary[tens]
    return name


def below_thousand(number):
    name = dictionary[number[0]] + 'hundred'
    if number[1] == '0' and number[2] != '0':
        name += 'and' + below_ten(number[2])
    elif number[1] != '0':
        name += 'and' + below_hundred(number[1:])
    return name


count = 0
names = []
for i in range(1, 1001):
    number_string = str(i)
    length = len(number_string)
    if i < 10:
        name = below_ten(number_string)
    elif i < 100 >= 10:
        name = below_hundred(number_string)
    elif i < 1000 >= 100:
        name = below_thousand(number_string)
    else:
        name = 'onethousand'
    names.append(name)
    count += len(name)

print(count)
