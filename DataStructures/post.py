#!/usr/bin/python3
#Jeanna Shellenberger
#CS 260 - Section 001
#2/4/2019
#infix, postfix, and prefix reader

from lexer import *

class init_tree():
    def __init__(self, parent = None, right = None, left = None):
        self.node = parent
        self.left = left
        self.right = right

def parse():
    operators = ['*','+','/','-','(',')']
    stack = []
    token = get_next_token()

    while token:
        if token in operators:
            right = stack.pop()
            left = stack.pop()
            stack.append(init_tree(token,right,left))
        else:
            stack.append(init_tree(token))

        token = get_next_token()

    return stack.pop()

def postfix(init_tree):
    if init_tree is not None:
        return str(postfix(init_tree.left)) + str(postfix(init_tree.right)) + str(init_tree.node)
    return ''

def prefix(init_tree):
    if init_tree is not None:
        return str(init_tree.node) + str(prefix(init_tree.left)) + str(postfix(init_tree.right))
    return ''

def infix(init_tree):
    if init_tree is not None:
        return str(prefix(init_tree.left)) + str(init_tree.node) + str(postfix(init_tree.right))
    return ''

if __name__ == "__main__":
    while get_expression() is True:
        mk_tree = parse()
        print("Postfix: " + str(postfix(mk_tree)))
        print("Prefix: " + str(prefix(mk_tree)))
        print("Infix: " + str(infix(mk_tree)))

    print (mk_tree)
