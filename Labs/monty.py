#Jeanna Shellenberger Section 061
import random   #need this for randomizing the seed
import sys   #need this just incase exit() decides not to work

#Lists
doors = ['G', 'C', 'G']
num = [1, 2, 3]

#Seed input and test for randomization
s = input('Enter Random Seed:\n')
try:
    s = int(s)
    random.seed(s)
except ValueError:
    print('Seed is not a number!')
    sys.exit()

#welcome
print('Welcome to Monty Hall Analysis')
print("Enter 'exit' to quit.")

#Input
t = input('How many tests should we run?\n') #number of tests
while t.lower() != 'exit': #makes sure case is not an issue with exit
    stay = 0 #variables to help test
    switch = 0
    c = 0 #c for choices
    try:
        t = int(t)
    except ValueError:  #make sure it's a number
        t = input('Please enter a number:\n')
        continue
    if t <= 10: #prevent overflow by spliting tests above or below ten
        for c in range (c, t): #make sure to hit all tests
            random.seed(s)
            print('Game', c + 1) #output for games
            random.shuffle(doors)
            print('Doors', doors) #out put for door
            random.seed()
            player = random.choice(num) #allows the 'player' to randomly select a door
            print('Player selects Door', player) #out put for the player selected door
            monty = random.choice(num)  #allows 'monty' to randomly select a door
            while monty == player or monty == (doors.index('C') + 1): #ensures that monty and the player don't select the same door
                monty = random.choice(num)
            print('Monty selects Door', monty) #outputs monty's door choice
            if player == (doors.index('C') +1): #calculatess which is better
                print('Player should stay to win.')
                stay += 1
            else:
                print('Player should switch to win.')
                switch += 1
        stay_percent = (stay / t) * 100 #calculates win percentage
        switch_percent = (switch / t) * 100
        print('Stay Won', round(stay_percent, 1), '% of the time.') #outputs win percentage
        print('Switch Won', round(switch_percent, 1), '% of the time.')
    elif t > 10: #prevents overflow by splitting tests above or below ten
        for c in range(c, t): #same calculations as below ten
            random.seed(s)
            random.shuffle(doors)
            random.seed()
            player = random.choice(num)
            monty = random.choice(num)
            while monty == player or monty == (doors.index('C') + 1):
                monty = random.choice(num)
            if player == (doors.index('C') + 1):
                stay += 1
            else:
                switch += 1
        stay_percent = (stay / t) * 100 #calculates win percentage
        switch_percent = (switch / t) * 100
        print('Stay Won', round(stay_percent, 1), '% of the time.') #outputs win percentage
        print('Switch Won', round(switch_percent, 1), '% of the time.')
    t = input('How many tests should we run?\n') #makes sure the test loops until 'exit' is entered

print('Thank you for using this program.') #program end
