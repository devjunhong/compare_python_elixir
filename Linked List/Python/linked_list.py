#!/usr/bin/python

class Node(object): 
	def __init__(self, data):
		self.data = data
		self.next_node = None 

class LinkedList(object): 
	def __init__(self, node): 
		self.head = node

	def add_end(self, value): 
		""" Add other node to the end of the list. 

		Keyword arguments: 
		value -- Create a node with this value and append to the end.
		"""
		node = Node(value)
		tail = self.head

		while tail.next_node is not None: 
			tail = tail.next_node 

		tail.next_node = node

	def add_first(self, value): 
		""" Add other node to the first of the list. 

		Keyworad arguments: 
		value -- Create a node with this value and append to the end.
		"""
		node = Node(value)
		node.next_node = self.head
		self.head = node

	def add_given(self, value, given): 
		""" Add other node to the next of given value. 

		Keyword arguments: 
		node -- A node that will be next to the node matching 
		with the value. 
		value -- A value that indicate the node.
		"""
		node = Node(value)
		value_node = self.head 

		while (value_node is not None and 
			value_node.data != given): 
			value_node = value_node.next_node 

		node.next_node = value_node.next_node 
		value_node.next_node = node

	def delete(self, data):
		""" Delete the node same with data from the list. 

		Keyword arguments: 
		data -- A node with equal data will be deleted. 
		""" 
		tail = self.head 
		prev = self.head 

		while tail.next_node is not None: 
			prev = tail
			tail = tail.next_node 

			if tail.data == data: 
				prev.next_node = tail.next_node 

	def delete_nth(self, n): 
		""" Delete the node that occurs with n th position. 

		Keyword arguments: 
		n -- A number that indicates the position of the list.
		"""
		if n == 1: 
			self.head = self.head.next
		else:
			node = self.head

			while(node):
				n -= 1
				if n == 1:
					if node.next_node is None: 
						node.next_node = None
					else:
						node.next_node = node.next_node.next_node
					break
				node = node.next_node

	def to_string(self): 
		""" Print out internal data to the console. """
		node = self.head 

		while node is not None: 
			print("\t", node.data) 
			node = node.next_node

def main():
	head = Node(-1)
	linked = LinkedList(head)

	# Create continuous node to head 
	for i in range(0, 5):
		linked.add_end(i)

	# Printing out the result 
	print("Print Linked List Iterate Result")
	# expected to show -1, 0, 1, 2, 3, 4
	linked.to_string()	

	print("After removing 3")
	linked.delete(3)
	# expected to show -1, 0, 1, 2, 4
	linked.to_string()

	print("After removing 4 and adding first 5") 
	linked.delete(4) 
	linked.add_first(5)
	# expected to show 5, -1, 0, 1, 2
	linked.to_string()

	print("After inserting 100 to next to the 0") 
	linked.add_given(100, 0)
	# expected to show 5, -1, 0, 100, 1, 2
	linked.to_string()

	print("After removing second item(-1)") 
	linked.delete_nth(2)
	# expected to show 5, -1, 100, 1, 2
	linked.to_string()

if __name__ == "__main__":
	main() 