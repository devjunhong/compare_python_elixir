#!/usr/bin/python3

def main():
	print("Graph with adjacency matrix")
	
	g = [[0, 1, 0, 0, 1], 
	[1, 0, 1, 1, 1], 
	[0, 1, 0, 1, 0], 
	[0, 1, 1, 0, 1],
	[1, 1, 0, 1, 0]]

	for r in g:
		for c in r:
			print(c, end=' ')
		print() 

if __name__ == "__main__":
	main() 