#!/usr/bin/python

#Jeanna Shellenberger - jls825
#CS 260 - Section 001
#2/11/2019
#Constructs a heap

import timeit

#sorts the array into a heap
def Make_Heap(array):
    for i in range((len(array) - 1)// 2, -1, -1):
        Down_Heap(i, array)

    return array

#inserts new node into the bottom and moves it up if it is larger than its parent
def Down_Heap(i, array):
    if Left(i) > len(array) - 1:
        return -1
    li = Left(i)
    if (Right(i) <= (len(array) - 1)) and (array[li] < array[Right(i)]):
        li = Right(i)

    if array[i] < array[li]:
        Swap(array, i, li)
        Down_Heap(li, array)

#downheap the nodes
def Swap(array, i, li):
    array[i], array[li] = array[li], array[i]

#find left node
def Left(i):
    return (2*i)+1

#find right node
def Right(i):
    return (2*i)+2

#format table
if __name__ == "__main__":
    arr = []
    print("   n            T(n)")
    for i in range(10):
        arr.append(i)
    timer = timeit.Timer("Make_Heap(arr)", "from __main__ import Make_Heap, arr")
    delta = timer.timeit(1)
    print("10", delta)

    for i in range(20):
        arr.append(i)
    timer = timeit.Timer("Make_Heap(arr)", "from __main__ import Make_Heap, arr")
    delta = timer.timeit(1)
    print("20", delta)

    for i in range(30):
        arr.append(i)
    timer = timeit.Timer("Make_Heap(arr)", "from __main__ import Make_Heap, arr")
    delta = timer.timeit(1)
    print("30", delta)

    for i in range(40):
        arr.append(i)
    timer = timeit.Timer("Make_Heap(arr)", "from __main__ import Make_Heap, arr")
    delta = timer.timeit(1)
    print("40", delta)

    for i in range(50):
        arr.append(i)
    timer = timeit.Timer("Make_Heap(arr)", "from __main__ import Make_Heap, arr")
    delta = timer.timeit(1)
    print("50", delta)

    for i in range(60):
        arr.append(i)
    timer = timeit.Timer("Make_Heap(arr)", "from __main__ import Make_Heap, arr")
    delta = timer.timeit(1)
    print("60", delta)

    for i in range(70):
        arr.append(i)
    timer = timeit.Timer("Make_Heap(arr)", "from __main__ import Make_Heap, arr")
    delta = timer.timeit(1)
    print("70", delta)

    for i in range(80):
        arr.append(i)
    timer = timeit.Timer("Make_Heap(arr)", "from __main__ import Make_Heap, arr")
    delta = timer.timeit(1)
    print("80", delta)

    for i in range(90):
        arr.append(i)
    timer = timeit.Timer("Make_Heap(arr)", "from __main__ import Make_Heap, arr")
    delta = timer.timeit(1)
    print("90", delta)

    for i in range(100):
        arr.append(i)
    timer = timeit.Timer("Make_Heap(arr)", "from __main__ import Make_Heap, arr")
    delta = timer.timeit(1)
    print("100", delta)
