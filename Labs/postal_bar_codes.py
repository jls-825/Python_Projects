#Jeanna Shellenberger Section 061
digit_dict = {1: ':::||', 2: '::|:|', 3: '::||:', 4: ':|::|', 5: ':|:|:', 6: ':||::', 7: '|:::|', 8: '|::|:',
              9: '|:|::', 0: '||:::'}
var = True


def checksum(zip):
    res = sum(int(x) for x in zip if x.isdigit())
    rem = 10 - res % 10
    if rem == 10:
        rem = 0
    return str(rem)


def barcode(zip):
    bcode = '|'
    for x in zip:
        bcode += digit_dict[int(x)]
    bcode += digit_dict[int(checksum(zip))] + '|'
    return bcode


if __name__ == '__main__':
    print('Welcome to Bar Code Generator')
    while var == True:
        message = input('Enter Zip Code (exit to quit):\n')
        if message.lower() == 'exit':
            var = False
        else:
            print('Bar Code:')
            finalmessage = barcode(message)
            print(finalmessage)
    print('Thanks for using me.')
