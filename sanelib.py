#Jeanna Shellenberger Section 061
import sys
print('Welcome to a fun word replacement game.')
try: #checks for a readable file
    txt_file = input('Enter the name of the file to use:\n') #asks for input
    open_file = open(txt_file, 'r') #opens file
    file = open_file.read() #reads file
except OSError: #if file cant be read
    print('Error Bad File Name')
    sys.exit()

v = ['a', 'e', 'i', 'o', 'u'] #and sometimes y
story = ''

#loop
for word in file.split(' '): #splits file at spaces
    ask = ''
    if word[0] == '[': #finds the bigging bracket
        ask = word[1:word.index(']')]  #finds the end bracket
        if ask[0] in v: #makes sure to use 'an'
            lib = input('Please give an ' + ask + '\n')
        else: #makes sure to use 'a'
            lib = input('Please give a ' + ask + '\n')
        story += lib + word[word.index(']') + 1:len(word)] + ' ' #reassembles story
    else:
        story  += word + ' ' #makes sure to include spaces

#finished
print('Here is your story!')
print(story)


