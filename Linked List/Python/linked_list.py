#!/usr/bin/python
from node import Node
from list import LinkedList

def initialize():
	head = Node(-1)
	linked = LinkedList(head)

	# Create continuous node to head 
	for i in range(0, 5):
		linked.add_end(i)

	# Printing out the result 
	print("Print Linked List Iterate Result")
	# expected to show) -1, 0, 1, 2, 3, 4
	linked.to_string()	

	return head, linked

def test_remove(linked_list):
	print("1. After removing 3")
	linked_list.delete(3)
	# expected to show) -1, 0, 1, 2, 4
	linked_list.to_string()

def test_remove_after(linked_list):
	print("2. After removing 4") 
	linked_list.delete(4) 
	# expected to show) -1, 0, 1, 2, 4
	linked_list.to_string()

def test_add_first(linked_list):
	print("3. Add first 5")
	linked_list.add_first(5)
	# expected to show) 5, -1, 0, 1, 2
	linked_list.to_string()

def test_insert_next(linked_list):
	print("4. After inserting 100 to next to the 0") 
	linked_list.add_given(100, 0)
	# expected to show) 5, -1, 0, 100, 1, 2
	linked_list.to_string()

def test_remove_index(linked_list):
	print("5. After removing second item(-1)") 
	linked_list.delete_nth(2)
	# expected to show) 5, 0, 100, 1, 2
	linked_list.to_string()

def test_length(linked_list):
	# expected to show) 5
	print("length>>", linked_list.get_legnth())

def test_length_recursive(linked_list):
	print("recursive length >>", linked_list.get_length_rec())

def test_swap(linked_list):
	print("Swapping 0 and 1")
	linked_list.swapping(0, 1)
	# expected to show) 5, 1, 100, 0, 2
	linked_list.to_string()
	
	print("Swapping -1 and 0 ) expecting no change")
	linked_list.swapping(-1, 0)
	# expected to show) 5, 1, 100, 0, 2
	linked_list.to_string()

	print("Swapping 5 and 0 ) see head is changed")
	linked_list.swapping(5, 0)
	# expected to show) 0, 1, 100, 5, 2
	linked_list.to_string()

def main():
	head, linked = initialize()

	test_remove(linked)
	test_remove_after(linked)
	test_add_first(linked)
	test_insert_next(linked)
	test_remove_index(linked)
	test_length(linked)
	test_length_recursive(linked)
	test_swap(linked)
	assert(False)

if __name__ == "__main__":
	main() 