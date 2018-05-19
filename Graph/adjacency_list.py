#!/usr/bin/python3

def initialize(vertices):
	"""
	Return initialized graph with 
	specifying vertex number

	@type: vertices, integer
	@param: vertices, number of vertices
	"""
	g = [None] * vertices

	for i in range(0, vertices):
		g[i] = []

	return g

def add(g, start, end):
	"""
	Add edge information into g

	@type: g, graph (2D array)
	@param: g, adjacency list
	@type: start, integer
	@param: start, start vertex point for edge 
	@type: end, integer
	@param: end, end vertex point for edge
	"""
	g[start].append(end)

	return g

def print_graph(g):
	"""
	Print the adjacency list graph

	@type: g, graph (2D array)
	@param: g, adjacency lsit
	"""

	for v in range(0, len(g)):
		print("vertex [ ", v, " ]", end=' ')
		for e in range(0, len(g[v])):
			print(g[v][e], end=' ')
		print()
		
def main():

	print("Graph with adjacency matrix")

	v = 5
	g = initialize(v)

	g = add(g, 0, 1)
	g = add(g, 0, 4)
	g = add(g, 1, 0)
	g = add(g, 1, 4)
	g = add(g, 1, 2)
	g = add(g, 1, 3)
	g = add(g, 2, 1)
	g = add(g, 2, 3)
	g = add(g, 3, 1)
	g = add(g, 3, 4)
	g = add(g, 3, 2)
	g = add(g, 4, 3)
	g = add(g, 4, 0)
	g = add(g, 4, 1)
	
	print_graph(g)

if __name__ == "__main__":
	main() 