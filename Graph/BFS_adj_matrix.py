#!/usr/bin/python3

def BFS_search(g, v, start):
	"""
	Search using BFS

	@type: g, 2D array
	@param: g, graph (adjacency matrix) 
	@type: v, integer
	@param: v, number of vertex
	@type: start, integer
	@param: start, starting vertex
	"""

	visited = []
	wait = []

	while(v != len(visited)):
		print(start, end = ' -> ')
		visited.append(start)
		edges = g[start]
		for i in range(0, v):
			if edges[i] == 1:
				if ((i not in visited) and
					(i not in wait)):
					wait.append(i)
		start = wait.pop(0)

def print_graph(g):
	"""
	Print the graph

	@type: g, 2D array
	@param: g, graph (adjacency matrix) 
	"""

	for r in g:
		for c in r:
			print(c, end = ' ')
		print()

def main():
	print("BFS with adjacency matrix")
	print("Start from vertex 2")

	g = [[0, 1, 1, 0],
	[0, 0, 1, 0],
	[1, 0, 0, 1],
	[0, 0, 0, 1]]

	print_graph(g)
	BFS_search(g, 4, 2)

if __name__ == "__main__":
	main()