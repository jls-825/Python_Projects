#Interface Class for a Stack
#Only allows access to the
#Stack commands of the built in list
class Stack:
	#Create a New Empty Stack
	def __init__(self):
		self.__S = []
	#Display the Stack
	def __str__(self):
		return str(self.__S)
	#Add a new element to top of stack
	def push(self,x):
		self.__S.append(x)
	#Remove the top element from stack
	def pop(self):
		return self.__S.pop()
	#See what element is on top of stack
	#Leaves stack unchanged
	def top(self):
		return self.__S[-1]


print('Welcome to Postfix Calculator')
print('Enter exit to quit.')

def postfix(exp):
    for i in exp.split():
        try:
            object.push(float(i))
        except ValueError:
            val2 = object.pop()
            val1 = object.pop()
            if i == '+':
                object.push(val1 + val2)
            if i == '-':
                object.push(val1 - val2)
            if i == '*':
                object.push(val1 * val2)
            if i == '/':
                object.push(val1 / val2)
    return object.top()


while True:
    object = Stack()
    a = input('Enter Expression:\n')
    if a.lower() != 'exit':
        print('Result:',postfix(a))
    else:
        exit(0)

