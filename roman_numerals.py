#Jeanna Shellenberger Section 061
def roman(num, one, five, ten):
    num = int(num)
    if num == 0:
        return ''
    elif num == 1:
        return str(one)
    elif num == 2:
        return str(one + one)
    elif num == 3:
        return str(one + one + one)
    elif num == 4:
        return str(one + five)
    elif num == 5:
        return str(five)
    elif num == 6:
        return str(five + one)
    elif num == 7:
        return str(five + one + one)
    elif num == 8:
        return str(five + one + one + one)
    elif num == 9:
        return str(one + ten)


def roman_num(num):
    num = str(num)
    while len(num) < 4:
        num = '0' + num
    return str(roman(num[0], 'M', 'v', 'x')) + str(roman(num[1], 'C', 'D', 'M')) + str(
        roman(num[2], 'X', 'L', 'C')) + str(roman(num[3], 'I', 'V', 'X'))


if __name__ == "__main__":
    print('Roman Number Generator. Enter 0 to quit.')
    while True:
        number = input('Enter a number between 1 and 9,999:\n')
        try:
            number = int(number)
            if number == 0:
                break
            number = str(number)
            print('Roman Numerals:', roman_num(number))
        except:
            continue
    print('Roman Numerals: \nBye.')