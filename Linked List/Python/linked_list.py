#!/usr/bin/python

class Node(object): 
	def __init__(self, data):
		self.data = data
		self.nextNode = None 

class LinkedList(object): 
	def __init__(self, node): 
		self.head = node

	def add(self, node): 
		""" Add other node to the end of the list. 

		Keyword arguments: 
		node -- A node that will be added to tail of list.
		"""
		tail = self.head

		while tail.nextNode is not None: 
			tail = tail.nextNode 

		tail.nextNode = node

	def delete(self, data):
		""" Delete the node same with data from the list. 

		Keyword arguments: 
		data -- A node with equal data will be deleted. 
		""" 
		tail = self.head 
		prev = self.head 

		while tail.nextNode is not None: 
			prev = tail
			tail = tail.nextNode 

			if tail.data == data: 
				prev.nextNode = tail.nextNode 

	def to_string(self): 
		""" Print out internal data to the console. """
		node = self.head 

		while node is not None: 
			print(node.data) 
			node = node.nextNode

def main():
	head = Node(-1)
	linked = LinkedList(head)

	# Create continuous node to head 
	for i in range(0, 5):
		node = Node(i)
		linked.add(node)

	# Printing out the result 
	print("Print Linked List Iterate Result")

	# expected to show -1, 0, 1, 2, 3, 4
	linked.to_string()	

	print("After remove 9")
	linked.delete(9)

	# expected to show -1, 0, 1, 2, 3, 4
	linked.to_string()

	print("After remove 4") 
	linked.delete(4) 
	node = Node(5)
	linked.add(node)
	
	# expected to show -1, 0, 1, 2, 3, 5
	linked.to_string()
	print("hello") 

if __name__ == "__main__":
	main() 