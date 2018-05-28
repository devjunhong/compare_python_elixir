#!/usr/bin/python
from node import Node

class LinkedList(object): 
	def __init__(self, node): 
		self.head = node

	def add_end(self, value): 
		"""
		Add other node to the end of the list. 

		Keyword arguments: 
		value -- Create a node with this value and append to the end.
		"""
		node = Node(value)
		tail = self.head

		while tail.next_node is not None: 
			tail = tail.next_node 

		tail.next_node = node

	def add_first(self, value): 
		"""
		Add other node to the first of the list. 

		Keyworad arguments: 
		value -- Create a node with this value and append to the end.
		"""
		node = Node(value)
		node.next_node = self.head
		self.head = node

	def add_given(self, value, given): 
		"""
		Add other node to the next of given value. 

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
		""" 
		Delete the node same with data from the list. 

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
		""" 
		Delete the node that occurs with n th position. 

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

	def get_node_previous(self, target):
		""" 
		Get a node, value is target 
		and the previous node
		
		@type target: number
		@param target: find a node that has this value
		@return prev_node, target_node
		"""
		move_node = self.head
		prev_node = None

		while(move_node):
			if move_node.data == target:
				return prev_node, move_node
			prev_node = move_node
			move_node = move_node.next_node

		return None, None 

	def swap(self, prev_node1, node1, prev_node2, node2):
		"""
		Swap node1 and node2

		@type prev_node1: Node
		@param prev_node1: previous node for node1
		@type prev_node2: Node
		@param prev_node2: 
		"""
		temp = node2.next_node

		if prev_node1 is None:
			self.head = node2
		else:
			prev_node1.next_node = node2
		
		node2.next_node = node1.next_node 

		if prev_node2 is None:
			self.head = node1
		else:
			prev_node2.next_node = node1

		node1.next_node = temp

	def swapping(self, first, second): 
		""" Swapping the two value first and second."""
		first_prev_node, first_node = self.get_node_previous(first)
		second_prev_node, second_node = self.get_node_previous(second)

		# No first value in the list
		if (first_prev_node is None and first_node is None):
			return self

		# No second value in the list
		if (second_prev_node is None and second_node is None):
			return self

		# If the first and second value is same.
		if first_node == second_node:
			return self

		self.swap(first_prev_node, first_node, 
			second_prev_node, second_node)
				
		return self

	def reverse(self):
		""" Reversing the linked list """
		if self.head is None:
			return self		

		move = self.head
		prev = None

		while(move): 
			temp = move.next_node
			if temp is None: 
				self.head = move
			move.next_node = prev
			prev = move
			move = temp	

		return self

	def sorted_merge(self, other):
		""" Merge the sorted linked list """ 

		if self.head is None or other.head is None: 
			return self

		self_move = self.head 
		other_move = other.head

		new_head = None
		if self.head.data < other.head.data:
			new_head = Node(self.head.data)
			self_move = first_move.next_node
		else:
			new_head = Node(other.head.data)
			other_move = other_move.next_node 

		new_list = LinkedList(new_head)

		while(self_move and other_move):
			if self_move.data < other_move.data:
				new_list.add_end(self_move.data)
				self_move = self_move.next_node
			else:
				new_list.add_end(other_move.data)
				other_move = other_move.next_node

		if self_move is None:
			while(other_move):
				new_list.add_end(other_move.data)
				other_move = other_move.next_node

		if other_move is None: 
			while(self_move):
				new_list.add_end(self_move.data)
				self_move = self_move.next_node

		return new_list