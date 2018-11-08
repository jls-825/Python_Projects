print('Welcome to Fun with Fraactions!')

a = True
while a == True:
    try:
        n = input('Enter number of iterations (integer > 0):\n')
        n = int(n)
        a = False
    except:
        continue
