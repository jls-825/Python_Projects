#Jeanna Shellenberger Section 061
print('Welcome to the length conversion wizard.')
print('This program can convert between any of the following lengths.')
print('inches\nfeet\nyards\nmiles\nleagues\ncentimeters\ndecimeters\nmeters\ndecameters\nhectometers\nkilometers')
print('Note: You must use the units exactly as spelled above.')

units = { #list of units
    'inches': 1,
    'feet': 1 / 12,
    'yards': (1 / 12) / 3,
    'miles': (1 /12) / 5280,
    'leagues': ((1 /12) / 5280) / 3,
    'centimeters': 2.54,
    'decimeters': 2.54 / 10,
    'meters': 2.54 / 100,
    'decameters': 2.54 / 1000,
    'hectometers': 2.54 / 10000,
    'kilometers': 2.54/ 100000,
}

numStart = float(input('\nEnter value:')) #starting number of units
unitsFrom = str(input('Enter from units:')) #original units
unitsTo = str(input('Enter to units:')) #converted units

numFinish = ((1 / units[unitsFrom]) * numStart) * units[unitsTo] #takes the starting nuber of units and creates the final number

print(numStart, unitsFrom, 'is', round(numFinish,4),unitsTo)

