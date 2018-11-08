#Jeanna Shellenberger Section 061
def twoscomp(num):
    a = False
    count = 0
    num = str(num[::-1])
    comp = ''
    t = ''
    x = False
    for i in range(len(num)):
        if num[i] == '0':
            comp += '1'
        elif num[i] == '1':
            comp += '0'
    while a == False:
        if x == False:
            if comp[count] == '0':
                t += '1'
                count += 1
                x = True
            elif comp[count] == '1':
                t += '0'
                count += 1
        elif x == True:
            t += comp[count]
            count += 1
        if count >= len(comp):
            a = True
    f = t[::-1]
    return f

if __name__ == "__main__":
    print("Welcome to Two's Complement Creator")
    store = input('Enter a Binary Value:\n')
    res = twoscomp(store)
    print("In Two's Complement:")
    print(res)
