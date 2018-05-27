#!/usr/bin/python3

def DFS_rec(g, s, visited):
	"""
	Search by DFS method 

	@type: g, 2D array 
	@param: g, graph (adjacency matrix)
	@type: s, integer
	@param: s, indiate the vertex to visit
	@type: visited, list
	@param: visited, make a list to store the visited
	"""
	print(s, end = ' -> ')
	visited.append(s)
	adj = g[s]

	for i in range(0, len(adj)):
		if adj[i] == 1:
			if i not in visited:
				DFS_rec(g, i, visited)

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
	print("DFS with adjacency matrix")
	print("Start from vertex 2")

	g = [[0, 1, 1, 0],
	[0, 0, 1, 0],
	[1, 0, 0, 1],
	[0, 0, 0, 1]]

	print_graph(g)

	print("DFS recursive version")

	DFS_rec(g, 2, [])

if __name__ == "__main__":
	main() 