#Jeanna Shellenberger Section 068

#import class
from socialite import socialite

#welcome
print('Welcome to CS 172: Socialite Homework')

#loop for good input
a = True
while a == True:
    try:
        num = input('How many Socialites do you want to create?\n')
        num = int(num)
        a = False
    except:
        print('Invalid Input')
        continue

#list of the total users
TotalUsers = []

#ask for socialite input
for i in range(num):
    user = socialite()
    print("Enter Data for Socialite", i+1)
    user.setFirstName(input("Enter First Name:\n"))
    user.setLastName(input("Enter Last Name:\n"))
    user.setUserID(input("Enter User ID:\n"))
    user.setPicture(input("Enter URL for Picture:\n"))
    user.setWebsite(input("Enter URL for Website:\n"))
    user.setDescription(input("Enter Website Description:\n"))
    TotalUsers.append(user)
    print("Socialite Created\n")

#print socialite info
print('====Socialite Information====')
for person in TotalUsers:
    print(person.str())
    print()

