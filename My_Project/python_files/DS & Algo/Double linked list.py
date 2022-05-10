class Node:

	def __init__(self, data):
		## previous pointer
		self.prev = None

		## data of the node
		self.data = data

		## next pointer
		self.next = None

class LinkedList:

	def __init__(self):
		## initializing the head with None
		self.head = None

	def insert(self, new_node):
		## check whether the head is empty or not
		if self.head:
			## getting the last node
			last_node = self.head
			while last_node.next != None:
				last_node = last_node.next

			## assigning the last node to the previous pointer of the new node
			new_node.prev = last_node

			## assigning the new node to the next pointer of last node
			last_node.next = new_node

	def display(self):
		## printing the data in normal order
		print("Normal Order: ", end='')

		temp_node = self.head
		while temp_node != None:
			print(temp_node.data, end=' ')
			temp_node = temp_node.next
		print()

		## printing the data in reverse order using previous pointer
		print("Reverse Order: ", end='')

		## getting the last node
		last_node = self.head
		while last_node.next != None:
			last_node = last_node.next

		temp_node = last_node
		while temp_node != None:
			print(temp_node.data, end=' ')
			temp_node = temp_node.prev
		print()
