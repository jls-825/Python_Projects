from Birthday import Birthday
birthdays = []

for i in range(12):
    table.append([])

with open('bdaylist.txt') as file__:
    for line in file.__readlines():
        x = line.split('/')

for i in range(len(birthdays)):
    b_day = birthdays[i]
    hash = b_day.__hash__()
    print('Hash location', i, 'has', hash, 'elements in it')
