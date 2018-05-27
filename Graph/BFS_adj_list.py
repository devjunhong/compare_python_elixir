#!/usr/bin/python3
from collections import defaultdict

class Graph(object):
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		"""
		Add edge from u to v

		@type: u, integer
		@param: u, start vertex
		@type: v, integer
		@param: v, end vertex
		"""
		self.graph[u].append(v)

	def BFS(self, s):
		"""
		BFS search with graph

		@type: s, integer
		@param: s, start vertex
		"""
		wait = [s]
		visited = [s]

		while (len(wait) != 0):
			u = wait.pop(0)
			visited.append(u)
			print(u, end=' -> ')
			adj = self.graph[u]

			for v in adj:
				if v not in visited:
					wait.append(v)

	def print_graph(self):
		for k, v in self.graph.items():
			print(k, v)

def main():
	g = Graph()

	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	g.addEdge(2, 0)
	g.addEdge(2, 3)
	g.addEdge(3, 3)

	g.print_graph()
	g.BFS(2)

if __name__ == "__main__":
	main() 