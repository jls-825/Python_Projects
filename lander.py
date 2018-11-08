#Jeanna Shellenberger Section 061
import sys
a = True #check
Level = 0 #level count
G = 0 #gravity
F = 0 #fuel
A = 50 #meters above the surface
V = 0 #initial velocity m/s
s = 0 #seconds passed
T = 0.1 #acceleration of the thrusters m/s^2
name = ''

def ask_fuel(current_fuel): #asks for fuel and calculates values
    global Level #preventing errors
    global A
    global V
    global name
    global G
    global F
    global T
    global s
    b = True #check
    while b == True:
        try:
            f = input('Enter units of fuel to use:\n')
            f = int(f)
            if 0 <= f <= current_fuel:
                a = True
                F = current_fuel - f
                V = (V + G) + (T * f)
                A = A + V
                s = s + 1
                b = False
                launch(F) #runs main outputs
            elif f < 0: #negative inputs
                print('Cannot use negative fuel.')
                b = True
            elif f > F: #not enough fuel!
                print('Not enough fuel. Max fuel:', F)
                b = True
        except ValueError:
            print('Please enter an integer')

def launch(F): #produces main output statments and outputs math
    global Level #preventing errors
    global A
    global V
    global s
    if 0 <= F and A > 0 : #mid-level
        print('After', s, 'seconds Altitude is', round(A,2), 'meters,', 'velocity is', round(V,2), 'm/s.')
        print('Remaining Fuel:', F, 'units.')
        ask_fuel(F)
    elif (A <= 0) and (-2 <= V <= 2): #success!
        A = 0
        print('After', s, 'seconds Altitude is', round(A,2), 'meters,', 'velocity is', round(V,2), 'm/s')
        print('Remaining Fuel:', F, 'units.')
        print('Landed Successfully')
        A = 50
        V = 0
        s = 0
        return (A, V, s)
    else: #crash!!!
        A = 0
        print('After', s, 'seconds Altitude is', round(A,2), 'meters,', 'velocity is', round(V,2), 'm/s')
        print('Remaining Fuel:', F, 'units.')
        print('Crashed!')
        Level = Level - 1
        A = 50
        V = 0
        s = 0
        return (Level, A, V, s)

def play_level(name, G, F): #welcome to the level, now go!
    print('Entering Level', Level)
    print('Landing on the', name)
    print('Gravity is', G, 'm/s^2')
    print('Initial Altitude:', A, 'meters')
    print('Initial Velocity:', V, 'm/s')
    print('Burning a unit of fuel causes', T, 'm/s slowdown.')
    print('Initial Fuel Level:', F, 'units')
    print('\nGO')
    ask_fuel(F)

#Welcome
print('Welcome to Lunar Lander.')
while a == True: #level counter
    if Level < 11:
        print('Do you want to play level',Level + 1,'?(yes/no)')
        ans = input()
        ans = ans.lower()
    else:
        print('Thank You For Playing')
        sys.exit()

    if ans == 'yes': #changes levels and variables
        Level = Level + 1
        if Level == 1:# moon
            name = 'Moon'
            G = -1.62  # acceleration of gravity m/s^2
            F = 150  # amount of fuel
        elif Level == 2: # earth
            name = 'Earth'
            G = -9.81  # acceleration of gravity m/s^2
            F = 5000  # amount of fuel
        elif Level == 3:  # pluto
            name = 'Pluto'
            G = -0.42  # acceleration of gravity m/s^2
            F = 1000  # amount of fuel
        elif Level == 4: # neptune
            name = 'Neptune'
            G = -14.07  # acceleration of gravity m/s^2
            F = 1000  # amount of fuel
        elif Level == 5:  # uranus
            name = 'Uranus'
            G = -10.67  # acceleration of gravity m/s^2
            F = 1000  # amount of fuel
        elif Level == 6:  # saturn
            name = 'Saturn'
            G = -11.08  # acceleration of gravity m/s^2
            F = 1000  # amount of fuel
        elif Level == 7:  # jupiter
            name = 'Jupiter'
            G = -25.95  # acceleration of gravity m/s^2
            F = 1000  # amount of fuel
        elif Level == 8:  # mars
            name = 'Mars'
            G = -3.77  # acceleration of gravity m/s^2
            F = 1000  # amount of fuel
        elif Level == 9:  # venus
            name = 'Venus'
            G = -8.87  # acceleration of gravity m/s^2
            F = 1000  # amount of fuel
        elif Level == 10:  # mercury
            name = 'Mercury'
            G = -3.59  # acceleration of gravity m/s^2
            F = 1000  # amount of fuel
        elif Level == 11:  # sun
            name = 'Sun'
            G = -274.13  # acceleration of gravity m/s^2
            F = 50000  # amount of fuel
        a == False
        play_level(name, G, F)
    elif ans == 'no': #Good Bye
        print('You made it past',Level,'levels')
        print('Thank You For Playing')
        sys.exit()

