#!/usr/bin/python3
#Jeanna Shellenberger - jls825
#CS 260 - Section 001
#2/25/2019
#Implents Disjoint sets

#create the set
def Initialize(A):
    sets = {}

    #root is inside
    for i in A:
        sets[i] = i

    return sets

#returns the parent value
def Find(s,value):           
    if s[value] != value:
        s[value] = Find(s, s[value])

    return s[value]

def Merge(s, value1, value2):
    
    #get the root values
    val1_r = Find(s,value1)
    val2_r = Find(s,value2)

    #double check they are not the same
    if val1_r == val2_r:
        return

    if Size(s,val1_r) > Size(s,val2_r):
        s[val2_r] = val1_r
    else:
        s[val1_r] = val2_r

#find the size of the set
def Size(s,value):
    count = 1
    val_root = Find(s,value)
    for key in s:
        if s[key] == val_root:
            count += 1
    return count
