#Jeanna Shellenberger Section 068
import random
from enemy import enemy
from wyvern import wyvern
from skeleton import skeleton
from crab import giant_crab
from mermaid import mermaid
from hero import hero
commandList = ['sword','shield','fireball','potion','exit']
def combat(m1, m2):
    # reset health
    m1.resetHealth()
    m2.resetHealth()
    print("The Next Battle Begins: ")  # figure out who is battling
    print("You have encountered a:")
    print(m2.getName()+": "+m2.getDescription())

    attacker = None
    defender = None

    #Randomly select who starts
    start = random.randint(1, 2)
    if start == 1:
        attacker = m1
        defender = m2
        print("\n You spring into action.\n")
    else:
        attacker = m2
        defender = m1
        print("\n" + attacker.getName() + " catches you off guard.\n")

    print("\n"+attacker.getName()+" goes first.\n")

    # Loop until there is a winner
    while m1.getHealth() > 0 and m2.getHealth() > 0:
        if (m1 == attacker):
            while True:
                try:
                    n = input("Enter Command: sword, shield, fireball, potion, exit\n")
                    if n in commandList:
                        break
                except ValueError:
                    print('Please enter one of the listed commands.')
                continue
            if n.lower() == "sword":
                attacker.basicAttack(defender)
                print(attacker.getName(), "used", attacker.basicName(), "on", defender.getName())
            if n.lower() == "shield":
                attacker.defenseAttack(defender)
                print(attacker.getName(), "used", attacker.defenseName(), "on", defender.getName())
            if n.lower() == "fireball":
                attacker.specialAttack(defender)
                print(attacker.getName(), "used", attacker.specialName(), "on", defender.getName())
            if n.lower() == "potion":
                attacker.Heal()
                print(attacker.healName())
            if n.lower() == "exit":
                print("Thanks for playing!")
                exit()
            attacker.__str__()

        else:
            move = random.randint(1, 100)

            # print out who did what attack on who
            if 1 <= move <= 60:
                attacker.basicAttack(defender)
                print(attacker.getName(), "used", attacker.basicName(), "on", defender.getName())
            elif 61 <= move <= 80:
                attacker.defenseAttack(defender)
                print(attacker.getName(), "used", attacker.defenseName(), "on", defender.getName())
            else:
                attacker.specialAttack(defender)
                print(attacker.getName(), "used", attacker.specialName(), "on", defender.getName())

            if defender.getHealth() < 0:
                defender.resetHealth()
                defender.doDamage(defender.getHealth())

            print(attacker.getName(), "has", attacker.getHealth(), "health left.")

        # switch attacker with defender
        temp = attacker
        attacker = defender
        defender = temp

    # return who won
    return m1 if m1.getHealth() > 0 else m2

print("Welcome to Adventure Battle!")
n = input("What is the name of your hero?\n")
while True:
    try:
        r = input("How many monsters will " + n + " battle?\n")
        r = int(r)
        if r > 0:
            break
    except ValueError:
        print('Please enter an integer.')
        pass
count = 1
character = hero(n,150)
monsterList = []
for i in range(r):
    x = [giant_crab("Giant Crab",120),mermaid("Mermaid",200),skeleton("Skeleton",150),wyvern("Wyvern",200)]
    monsterList.append(random.choice(x))

print('=====Begin Dungeon Run=====')
for foe in monsterList:
    x = combat(character,foe)
    if x is not character:
        print("Defeat. Do not give up!")
        exit()
print("Congratulations! You Won!")
exit()
