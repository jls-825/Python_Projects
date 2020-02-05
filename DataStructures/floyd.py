#!/usr/bin/python3
#Jeanna Shellenberger - jls825
#CS 260 - Section 001
#3/4/2019
#Implements Floyd's all-pairs shortest-path algorithm

import sys

#get the data and foramt as a graph
def get_data():
	
	data = []
	
	#for each line in stdin add to the array
	for line in sys.stdin:
		data.append(line)

	graph = {}

	#read through data dont open file
	for line in data :
		adjacent = line.split()
		vertice = adjacent[0]
		graph[ vertice ] = {}
		adjacent.pop(0)
		for pos in adjacent:
			u,w = pos.split(',')
			if u not in graph:
				graph[u] = {}
			graph[vertice][u] = float(w)
	
	#return graph
	return graph

#create the distance and predicessor matrices
def init_matrices(graph):

    dist = [[float("inf") for column in graph] for row in graph]
    pred = [[0 for column in graph] for row in graph]

    #fill predecessor matrix with intial nodes
    for row in range(len(pred)):
        for column in range(len(pred)):
            pred[row][column] = row

    #fill in non existing postions
    for pos in range(len(dist)):
        dist[pos][pos] = 0

    for pos in range(len(pred)):
        pred[pos][pos] = "-"

    return (dist, pred)

#Floyd-Warshall Algorithm
def FW(graph, dist, pred):

    for node in graph:
        for element in graph[node]:
            pos1 = int(node)
            pos2 = int(element)
            data = graph[node][element]

            pred[pos1][pos2] = node
            dist[pos1][pos2] = int(data)
            dist[pos2][pos1] = int(data)

    #cycle through the matrices
    size = len(dist)
    for k in range(size):
        for i in range(size):
            for j in range(size):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    dist[j][i] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]
                    pred[j][i] = pred[k][j]

    print("\nDistance Matrix")
    display_matrix(dist)
    print("\nPredecessor Matrix")
    display_matrix(pred)

def display_matrix(matrix): 
   
    for size in range(len(matrix)):
        for pos in range(len(matrix)):
            print ("%3s" % matrix[size][pos], end=""),
        print()

if __name__ == "__main__":
    graph = get_data()

    dist, pred = init_matrices(graph)

    FW(graph, dist, pred)
