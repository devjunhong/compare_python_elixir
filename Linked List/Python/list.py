#!/usr/bin/python
from node import Node

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
		index = 0
		while node is not None: 
			print('\t[ {0} ]: {1}'.format(index, node.data)) 
			node = node.next_node
			index += 1

	def get_legnth(self): 
		""" Get a length of list with iterative manner. """
		node = self.head
		length = 0

		while (node):
			node = node.next_node 
			length += 1

		return length

	def get_length_rec(self):
		""" Get a length of list with recursive manner. """
		return self.get_length_rec_support(self.head)

	def get_length_rec_support(self, node):
		if node is None:
			return 0
		else:
			return 1 + self.get_length_rec_support(node.next_node)

	def swapping(self, first, second): 
		""" Swapping the two node first and second."""
		node = self.head

		first_node = None
		second_node = None
		first_prev_node = None 
		second_prev_node = None 

		while(node):
			if node.data == first:
				first_node = node
			elif node.data == second:
				second_node = node

			if node.next_node is not None: 
				if node.next_node.data == first:
					first_prev_node = node
				elif node.next_node.data == second:
					second_prev_node = node

			if first_prev_node and second_prev_node:
				break

			node = node.next_node

		if first_node and second_node:
			if first_prev_node and second_prev_node:
				temp = second_node.next_node

				first_prev_node.next_node = second_node 
				second_node.next_node = first_node.next_node 

				second_prev_node.next_node = first_node 
				first_node.next_node = temp 
			elif first_prev_node is None: 
				# first_node is head
				print(first_node.data, second_node.data)
				temp = first_node.next_node

				first_node.next_node = second_node.next_node
				second_prev_node.next_node = first_node

				second_node.next_node = temp
				self.head = second_node
			elif second_prev_node is None: 
				self.head = first_node
				temp = second_node.next_node

				second_node.next_node = first_node.next_node
				first_prev_node.next_node = second_node 

				first_node.next_node = temp